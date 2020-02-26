import csv
vett=[0,0,0,0,0,0,0,0,0,0,0,0]

with open('BILANCIAdataset400NUOVO.csv', mode='w') as dataset_file:
    games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    games_writer.writerow(["descr","Puzzle","Adventure", "Action", "RPG", "Simulation", "Strategy", "Shooter", "Sports", "Racing", "Educational", "Fighting", "BoardGames"])

with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if vett[10]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        if sum>1:
            i=0
            if vett[10]<=40 and int(row[11])==1   :

                while (i <= 11):
                    vett[i]=vett[i]+int(row[i+1])
                    i=i+1  

                with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                    games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                    dataset_file.close()

               
                                    
            print(f'{vett}')
csv_file.close()




with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if vett[10]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[10]<=299 and int(row[11])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()

with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[11]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[11]<=40 and int(row[12])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()

with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[11]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[11]<=299 and int(row[12])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                  
                print(f'{vett}')
csv_file.close()



with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[8]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[8]<=40 and int(row[9])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[8]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[8]<=299 and int(row[9])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()














with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[9]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[9]<=40 and int(row[10])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[9]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[9]<=299 and int(row[10])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()









with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[6]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[6]<=40 and int(row[7])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[6]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[6]<=299 and int(row[7])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()




with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[1]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[1]<=40 and int(row[2])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[1]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[1]<=299 and int(row[2])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()









with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[3]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[3]<=40 and int(row[4])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[3]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[3]<=299 and int(row[4])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()













with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[7]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[7]<=40 and int(row[8])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[7]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[7]<=299 and int(row[8])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()








with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[0]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[0]<=40 and int(row[1])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[0]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[0]<=299 and int(row[1])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()












with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[5]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[5]<=40 and int(row[6])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[5]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[5]<=299 and int(row[6])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()














with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[4]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[4]<=40 and int(row[5])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[4]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[4]<=299 and int(row[5])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()






















with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[2]>40:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum>1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[2]<=40 and int(row[3])==1  :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[2]>299:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[2]<=299 and int(row[3])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()






















with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count=0
    for row in csv_reader:
        if vett[1]>360:
            break
        if not (row):    
            continue
        if line_count == 0:
            line_count += 1  
            continue
   
        line_count+=1
        sum=0
        j=1
        while (j <= 12):
            sum=sum+int(row[j])
            j=j+1 
        
        if sum==1:
            i=0

            flag=0
            with open('BILANCIAdataset400NUOVO.csv') as indf:
                csv_reader1 = csv.reader(indf, delimiter=',')
                line=0
                for index in csv_reader1:
                    if not (index):    
                        continue
                    if line == 0:
                        line += 1  
                        continue
                    if row[0]==index[0]:
                        flag=1
                
            if flag==0:
                if vett[1]<=360 and int(row[2])==1 :

                    while (i <= 11):
                        vett[i]=vett[i]+int(row[i+1])
                        i=i+1  

                    with open('BILANCIAdataset400NUOVO.csv', mode='a') as dataset_file:
                        games_writer = csv.writer(dataset_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        games_writer.writerow([row[0],row[1],row[2] ,row[3],row[4],row[5], row[6],row[7], row[8], row[9],row[10] ,row[11],row[12]])
                        dataset_file.close()
                                        
                   
                print(f'{vett}')
csv_file.close()




