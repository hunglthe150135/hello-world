import matplotlib.pyplot as plt
import csv
from collections import Counter

def histogram():
    points = []
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    with open("SAMPLE_DATA_01.csv", "r", encoding="utf_8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            point = float(row['MAS291'])
            if point < 2:
                a+=1
            elif point >= 2 and point < 4:
                b+=1
            elif point >= 4 and point < 6:
                c+=1
            elif point >= 6 and point < 8:
                d+=1
            elif point >= 8 and point < 10:
                e+=1
    print(a, b, c, d, e)
    sum = a + b + c + d + e
    probability = [float(a/sum), float(b/sum), float(c/sum), float(d/sum), float(e/sum)]
    point = ['[0,2)', '[2,4)', '[4,6)', '[6,8)', '[8,10]']
    plt.bar(point, probability)
    plt.xticks(point)
    plt.yticks(probability) 
    plt.xlabel('Point')
    plt.ylabel('Probability')
    plt.show()
    



