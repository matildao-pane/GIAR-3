import csv


with open('dataset.csv', mode='w') as dataset_file:
    games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    games_writer.writerow(["descr","Puzzle","Adventure", "Action", "RPG", "Simulation", "Strategy", "Shooter", "Sports", "Racing", "Educational", "Fighting", "BoardGames"])

with open('GenrePrediction/data/gameClean.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count=0
    genreslist = ['Puzzle', 'Adventure', 'Action', 'RPG', 'Simulation', 'Strategy', 'Shooter', 'Sports', 'Racing', 'Educational', 'Fighting', 'BoardGames', ]
    for row in csv_reader:
        if not (row):    
            continue
        vett=[0,0,0,0,0,0,0,0,0,0,0,0]
        genres =row[3]
        genres = genres.replace("[",'').replace("]", "").replace("'","").replace(" ","")
        genres =list(genres.split(","))
        i=0
        for genre in genres:
#           i=i+1
#       if i>1:
#           count=count+1
#   print(f' {count} .')

          i=0
          print(genre)
          while (i <= 11):
              print(genre)
              if(genre==genreslist[i]):
                  vett[i]=1   
              i=i+1  
        with open('dataset.csv', mode='a') as dataset_file:
           games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
           games_writer.writerow([row[2],vett[0],vett[1],vett[2] ,vett[3],vett[4],vett[5], vett[6],vett[7], vett[8], vett[9],vett[10] ,vett[11]])
           dataset_file.close()