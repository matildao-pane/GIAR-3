package it.unipi.giar;

import java.io.File;
import java.io.FileNotFoundException;

import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import weka.classifiers.bayes.NaiveBayesMultinomialText;
import weka.classifiers.meta.FilteredClassifier;
import weka.core.Attribute;
import weka.core.DenseInstance;
import weka.core.Instances;
import weka.core.SerializationHelper;
import weka.core.converters.ArffSaver;
import weka.core.converters.ConverterUtils.DataSource;

public class GenrePrediction {
	
	static Instances [][] vettTrain = new Instances [10][12];	// vector of binary datasets TRAIN ONE PER EACH FOLD
	static Instances [] vettTest = new Instances [10];	// vector of datasets TEST ONE PER EACH FOLD
	
	static NaiveBayesMultinomialText [] vettNaive = new NaiveBayesMultinomialText[12];
	static FilteredClassifier [] vettSMO = new FilteredClassifier[12];
	static FilteredClassifier [] vettRandomForest = new FilteredClassifier[12];
	
	static int[][] confusionMatrix = new int[12][4];
	
	private static List<String> predictedGenres = new ArrayList<>();
	static{
		predictedGenres.add("prova");
	}
	
	public static void resetMatrix(int[][] mat) {
		for(int i=0; i<12; i++) {
			for(int j=0; j<12; j++) {
				mat[i][j]=0;
			}
		}
	}
	
	
	public static void printmatrices(int[][] mat) {
		for(int i=0; i<12; i++) {
			for(int j=0; j<4; j++) {
				if(j==2) {
					System.out.print("\n");
				}
				System.out.print(mat[i][j] + " ");
			}
			System.out.print("\n\n");
		}
		System.out.print("\n");
	}
	
	public static void printmatrix (int[][] mat, String classifier) {
		System.out.println("CONFUSION MATRIX " + classifier +"\n");
	
		for(int i=0; i<12; i++) {
			for(int j=0; j<12; j++) {
				System.out.print(mat[i][j] + " ");
			}
			System.out.print("\n");
		}
		System.out.print("\n");
	}
	
	
	
	
	public static void evaluate() {
		double[] precision= new double[12];
		double[] accuracy= new double[12];
		double[] recall = new double[12];
		double precisionavg,accuracyavg,recallavg,fmeasure,sum1=0,sum2=0,sum3=0;
		
		for(int i=0; i<12; i++) {
			double tp=confusionMatrix[i][0];
			double fn=confusionMatrix[i][1];
			double fp=confusionMatrix[i][2];
			double tn=confusionMatrix[i][3];
			
			precision[i]=tp/(tp+fp);
			
			recall[i]=tp/(tp+fn);
			
			accuracy[i]=(tp+tn)/(tp+fp+tn+fn);
			
			sum1 +=precision[i];
			sum2 +=recall[i];
			sum3 +=accuracy[i];
		}
		precisionavg=sum1/12;
		recallavg=sum2/12;
		accuracyavg=sum3/12;
		fmeasure=(2*precisionavg*recallavg)/(precisionavg+recallavg);
		//System.out.println("naivebayes");
		System.out.println("matrices");
		printmatrices(confusionMatrix);
		System.out.println("precision:" + precisionavg);
		System.out.println("recall:" + recallavg);
		System.out.println("accuracy:" + accuracyavg);
		System.out.println("fmeasure:" + fmeasure);
	}
	
	
	
	
	public static List<String> init(String descrizione) {
		List<String> genres = new ArrayList<>();
		genres.add("Puzzle");
		genres.add("Adventure");
		genres.add("Action");
		genres.add("RPG");
		genres.add("Simulation");
		genres.add("Strategy");
		genres.add("Shooter");
		genres.add("Sports");
		genres.add("Racing");
		genres.add("Educational");
		genres.add("Fighting");
		genres.add("BoardGames");
		

		createDatasets(genres);
		evaluate();
		//esporta tutti  modelli che sono nellarrray dei classificatori naive
		for(int z = 0; z < genres.size(); z++) {		
			try {
				SerializationHelper.write(new FileOutputStream("./src/main/resources/models/"+genres.get(z)+".model"), vettNaive[z]);
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
		
		return predictedGenres;
	}
	
	
	
	
	
	
	public static void createDatasets( List<String> genres){

			// Reading Entire Dataset
			DataSource source;
			try {
				source = new DataSource("src/main/resources/finaldataset.arff");
				Instances data = source.getDataSet();			
				
				// Randomize the dataset
				data.randomize(new Random(1)); 	 // randomize instance order before splitting dataset

				for(int i=0; i<10; i++){ // To calculate the results in each fold
					
					Instances test = data.testCV(10, i);
					Instances train = data.trainCV(10, i);
 
					//TO CHECK
					vettTest[i]=test;
		
					int numInstancesTrain = train.size();		
					
					System.out.println("fold: "+ i + " " +train.size() + ":train" + "test: " + test.size());
					
					//CREATION OF 12 BINARY DATATSETS (repeats this for every fold)
					createBinaryDatasets( genres, numInstancesTrain, train, i);	
					testNaive(test,genres);
	
				}	
					
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	}
	

	public static void createBinaryDatasets( List<String> genres,  int numInstances, Instances train, int foldnum) {
		try {
			for(int z = 0; z < genres.size(); z++) {	//12 generi		
				
				ArrayList<Attribute> attributes = new ArrayList<Attribute>();
				attributes.add(new Attribute("description", true));
				ArrayList<String> labels = new ArrayList<String>();
				labels.add("0");
				labels.add("1");
				
				attributes.add(new Attribute(genres.get(z),labels));
				

				Instances binTrainDataset = new Instances("Try", attributes, 400);
				binTrainDataset.setClassIndex(binTrainDataset.numAttributes() - 1);

				// adding instances		
				int class_count = 0;

				//insert the rows with genre!=other
				for ( int j = 0; j < numInstances; j++ ){	//per ogni riga del db		
					if(class_count<200) {
						double[] val = new double[2];
						val[0] = binTrainDataset.attribute(0).addStringValue(train.instance(j).stringValue(0));	//val0 prende la descr
						
						if(train.instance(j).value(z+1) == 1) {		
							val[1] = 1; 	//val1 prende 
							
							binTrainDataset.add(new DenseInstance(1.0, val));
							class_count++;
				
						}	
					}
				}
				
				//insert the rows with genre=other
				for ( int j = 0; j < numInstances; j++ ){	//per ogni riga del db				
					double[] val = new double[2];
					val[0] = binTrainDataset.attribute(0).addStringValue(train.instance(j).stringValue(0));

					if(!(train.instance(j).value(z+1) == 1)) {	
						if(class_count > 0) {
							val[1] = 0;
							binTrainDataset.add(new DenseInstance(1.0, val));
							class_count--;
						}
					}
					
					if(class_count == 0) {
						break;
					}			
				}
				
//			    ArffSaver saver = new ArffSaver();
//				 saver.setInstances(binTrainDataset);
//				 saver.setFile(new File("C:/Users/Matilde/Desktop/test"+z+".arff"));
//				 saver.writeBatch();

				
				/*
					//save in arff files to check on weka the results
					ArffSaver saver = new ArffSaver();
					saver.setInstances(binTrainDataset);
					try {
						saver.setFile(new File("src/main/resources/folds/fold" +foldnum +"/" + genres.get(z) + "_dataset.arff"));
						saver.writeBatch();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				 */
				
				vettTrain[foldnum][z] = binTrainDataset;	//save the db in the dbarray at genre z position	

				// train the classifier for this binary
				String[] options = weka.core.Utils.splitOptions("-W -P 0 -M 2.0 -norm 1.0 -lnorm 2.0 -lowercase -stopwords-handler weka.core.stopwords.Rainbow -tokenizer weka.core.tokenizers.AlphabeticTokenizer -stemmer \"weka.core.stemmers.SnowballStemmer -S porter\"");		
				vettNaive[z]= new NaiveBayesMultinomialText();
				vettNaive[z].setOptions(options);
				vettNaive[z].buildClassifier(binTrainDataset);
				
				
				
//				//smo
//				String[] options = weka.core.Utils.splitOptions("-F \"weka.filters.MultiFilter -F \\\"weka.filters.unsupervised.attribute.StringToWordVector -R 1 -W 1000 -prune-rate -1.0 -I -N 0 -L -stemmer \\\\\\\"weka.core.stemmers.SnowballStemmer -S porter\\\\\\\" -stopwords-handler weka.core.stopwords.Rainbow -M 2 -tokenizer weka.core.tokenizers.AlphabeticTokenizer\\\" -F \\\"weka.filters.supervised.attribute.AttributeSelection -E \\\\\\\"weka.attributeSelection.InfoGainAttributeEval \\\\\\\" -S \\\\\\\"weka.attributeSelection.Ranker -T -1.7976931348623157E308 -N -1\\\\\\\"\\\"\" -S 1 -W weka.classifiers.functions.SMO -- -C 1.0 -L 0.001 -P 1.0E-12 -N 0 -V -1 -W 1 -K \"weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007\" -calibrator \"weka.classifiers.functions.Logistic -R 1.0E-8 -M -1 -num-decimal-places 4\"");
//				vettSMO[z]= new FilteredClassifier();
//				vettSMO[z].setOptions(options);
//				vettSMO[z].buildClassifier(binTrainDataset);
//				
//				//randomForest				
//				String[] options = weka.core.Utils.splitOptions("-F \"weka.filters.MultiFilter -F \\\"weka.filters.unsupervised.attribute.StringToWordVector -R 1 -W 1000 -prune-rate -1.0 -I -N 0 -L -stemmer \\\\\\\"weka.core.stemmers.SnowballStemmer -S porter\\\\\\\" -stopwords-handler weka.core.stopwords.Rainbow -M 2 -tokenizer weka.core.tokenizers.AlphabeticTokenizer\\\" -F \\\"weka.filters.supervised.attribute.AttributeSelection -E \\\\\\\"weka.attributeSelection.InfoGainAttributeEval \\\\\\\" -S \\\\\\\"weka.attributeSelection.Ranker -T -1.7976931348623157E308 -N -1\\\\\\\"\\\"\" -S 1 -W weka.classifiers.trees.RandomForest -- -P 100 -I 100 -num-slots 1 -K 0 -M 1.0 -V 0.001 -S 944723357");
//				vettRandomForest[z]= new FilteredClassifier();
//				vettRandomForest[z].setOptions(options);
//				vettRandomForest[z].buildClassifier(binTrainDataset);
//				
//				
//				System.out.println("fold: "+ foldnum + " " +binTrainDataset.size() + ":bin" + "gener"+ genres.get(z));
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();

		}

	}
	
	public static void testNaive(Instances test, List<String> genres ) {
		try {
			for (int i = 0; i < test.numInstances();i++){		//per ogni riga del testset
				
//				System.out.println("test Instance "+ i);
//				System.out.println(test.instance(i));
			
				
				for(int z = 0; z < genres.size(); z++) {	//per ogni classificatore
					
					//crea datasetbinario con sola istanza 
					ArrayList<Attribute> attributes = new ArrayList<Attribute>();
					ArrayList<String> labels = new ArrayList<String>();
					labels.add("0");
					labels.add("1");
					attributes.add(new Attribute("description", true));
					attributes.add(new Attribute(genres.get(z),labels));
				
					Instances unlabeled = new Instances("Try", attributes, 1);	//1 num istanze
					unlabeled.setClassIndex(unlabeled.numAttributes() - 1);
					// adding instances			
					double[] val = new double[2];
					val[0] = unlabeled.attribute(0).addStringValue(test.instance(i).stringValue(0)); //val0 prende la descr
					val[1] = 0;	//nn importa tanto lo metto missing

					
					unlabeled.add(new DenseInstance(1.0, val));
					unlabeled.instance(0).setClassMissing(); 
					
					
//					System.out.println(genres.get(z));
//					System.out.println(i);
//					System.out.println(test.instance(i));
//					System.out.println(test.instance(i).stringValue(0));
//					System.out.println(attributes);
//					System.out.println(unlabeled);

					
					//classifica l'istanza con il classificatore z
					//il risultato mettilo in p
					int predicted;
					int expected;
					if(vettNaive[z].classifyInstance(unlabeled.instance(0)) == 1)
						predicted = 1;
					else
						predicted = 0;
					
					//metti in e l expected dell istanza i di test ma del genre z
					expected = (int)test.instance(i).value(z+1);
	
					
//					System.out.println("predicted: "+predicted);
//					System.out.println("exp: "+expected);
//					System.out.println(test.instance(i));
//					System.out.println((int)test.instance(i).value(z+1));
//					System.out.println(test.instance(i).attribute(z+1));
					
					//p e e fa tutti i controlli e scrivi nella conf mat z
					
					if (predicted==1 && expected ==1 ) {
						//tp
						confusionMatrix[z][0]++;
					}
					else if(predicted==0 && expected ==1 ) {
						//fn
						confusionMatrix[z][1]++;
					}
					else if(predicted==1 && expected ==0 ) {
						//fp
						confusionMatrix[z][2]++;
					}
					else if(predicted==0 && expected ==0 ) {
						//tn
						confusionMatrix[z][3]++;
					}
					
				
				}				
			}
	
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
}
					
		



	public static void testSMO(Instances test, List<String> genres ) {

		try {
			for (int i = 0; i < test.numInstances();i++){		//per ogni riga del testset
				
//				System.out.println("test Instance "+ i);
//				System.out.println(test.instance(i));
			
				
				for(int z = 0; z < genres.size(); z++) {	//per ogni classificatore
					
					//crea datasetbinario con sola istanza 
					ArrayList<Attribute> attributes = new ArrayList<Attribute>();
					ArrayList<String> labels = new ArrayList<String>();
					labels.add("0");
					labels.add("1");
					attributes.add(new Attribute("description", true));
					attributes.add(new Attribute(genres.get(z),labels));
				
					Instances unlabeled = new Instances("Try", attributes, 1);	//1 num istanze
					unlabeled.setClassIndex(unlabeled.numAttributes() - 1);
					// adding instances			
					double[] val = new double[2];
					val[0] = unlabeled.attribute(0).addStringValue(test.instance(i).stringValue(0)); //val0 prende la descr
					val[1] = 0;	//nn importa tanto lo metto missing

					
					unlabeled.add(new DenseInstance(1.0, val));
					unlabeled.instance(0).setClassMissing(); 
					
					
//					System.out.println(genres.get(z));
//					System.out.println(i);
//					System.out.println(test.instance(i));
//					System.out.println(test.instance(i).stringValue(0));
//					System.out.println(attributes);
//					System.out.println(unlabeled);

					
					//classifica l'istanza con il classificatore z
					//il risultato mettilo in p
					int predicted;
					int expected;
					if(vettSMO[z].classifyInstance(unlabeled.instance(0)) == 1)
						predicted = 1;
					else
						predicted = 0;
					
					//metti in e l expected dell istanza i di test ma del genre z
					expected = (int)test.instance(i).value(z+1);
	
					
//					System.out.println("predicted: "+predicted);
//					System.out.println("exp: "+expected);
//					System.out.println(test.instance(i));
//					System.out.println((int)test.instance(i).value(z+1));
//					System.out.println(test.instance(i).attribute(z+1));
					
					//p e e fa tutti i controlli e scrivi nella conf mat z
					
					if (predicted==1 && expected ==1 ) {
						//tp
						confusionMatrix[z][0]++;
					}
					else if(predicted==0 && expected ==1 ) {
						//fn
						confusionMatrix[z][1]++;
					}
					else if(predicted==1 && expected ==0 ) {
						//fp
						confusionMatrix[z][2]++;
					}
					else if(predicted==0 && expected ==0 ) {
						//tn
						confusionMatrix[z][3]++;
					}
					
				
				}				
			}
	
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
			
	}

	public static void testRandomForest(Instances test,  List<String> genres ) {
	
		try {
			for (int i = 0; i < test.numInstances();i++){		//per ogni riga del testset
				
//				System.out.println("test Instance "+ i);
//				System.out.println(test.instance(i));
			
				
				for(int z = 0; z < genres.size(); z++) {	//per ogni classificatore
					
					//crea datasetbinario con sola istanza 
					ArrayList<Attribute> attributes = new ArrayList<Attribute>();
					ArrayList<String> labels = new ArrayList<String>();
					labels.add("0");
					labels.add("1");
					attributes.add(new Attribute("description", true));
					attributes.add(new Attribute(genres.get(z),labels));
				
					Instances unlabeled = new Instances("Try", attributes, 1);	//1 num istanze
					unlabeled.setClassIndex(unlabeled.numAttributes() - 1);
					// adding instances			
					double[] val = new double[2];
					val[0] = unlabeled.attribute(0).addStringValue(test.instance(i).stringValue(0)); //val0 prende la descr
					val[1] = 0;	//nn importa tanto lo metto missing

					
					unlabeled.add(new DenseInstance(1.0, val));
					unlabeled.instance(0).setClassMissing(); 
					
					
//					System.out.println(genres.get(z));
//					System.out.println(i);
//					System.out.println(test.instance(i));
//					System.out.println(test.instance(i).stringValue(0));
//					System.out.println(attributes);
//					System.out.println(unlabeled);

					
					//classifica l'istanza con il classificatore z
					//il risultato mettilo in p
					int predicted;
					int expected;
					if(vettRandomForest[z].classifyInstance(unlabeled.instance(0)) == 1)
						predicted = 1;
					else
						predicted = 0;
					
					//metti in e l expected dell istanza i di test ma del genre z
					expected = (int)test.instance(i).value(z+1);
	
					
//					System.out.println("predicted: "+predicted);
//					System.out.println("exp: "+expected);
//					System.out.println(test.instance(i));
//					System.out.println((int)test.instance(i).value(z+1));
//					System.out.println(test.instance(i).attribute(z+1));
					
					//p e e fa tutti i controlli e scrivi nella conf mat z
					
					if (predicted==1 && expected ==1 ) {
						//tp
						confusionMatrix[z][0]++;
					}
					else if(predicted==0 && expected ==1 ) {
						//fn
						confusionMatrix[z][1]++;
					}
					else if(predicted==1 && expected ==0 ) {
						//fp
						confusionMatrix[z][2]++;
					}
					else if(predicted==0 && expected ==0 ) {
						//tn
						confusionMatrix[z][3]++;
					}
					
				
				}				
			}
	
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
		
		
	}
	
}