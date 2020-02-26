import csv



with open('dataset400.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count=0
    line_count=0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1  
            continue
        if not (row):    
            continue
        vett=[0,0,0,0,0,0,0,0,0,0,0,0]
        i=1
        x=0
        while(i<12):
            vett[i-1]=row[i]
            i=i+1
        for t in vett:
            x=x+int(t)
        if x > 1:
            count=count+1
    print(f' {count} .')
