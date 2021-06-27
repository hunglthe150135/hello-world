import csv

with open('SAMPLE_DATA_01.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)


