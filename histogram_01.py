import csv
import pandas as pd
from matplotlib import pyplot as plt, pyplot
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

class input:
  def __init__(self):
      self.data = {
          'id': [],
          'mas291': []
      }

      with open("SAMPLE_DATA_01.csv", "r", encoding="utf_8") as file:
          csv_reader = csv.DictReader(file)
          for row in csv_reader:
               self.data['id'].append(row['ID'])
               self.data['mas291'].append(float(row['MAS291']))

input_sample_data_01 = input()
print(input_sample_data_01.data)



plt.style.use('fivethirtyeight')


data = pd.read_csv('SAMPLE_DATA_01.csv')

ids = data['ID']
grades = data['MAS291']

bins = [0,2.2,4.4,6.6,8.8,10]

plt.hist(grades, bins=bins, edgecolor='black')

median_grade = 5
color = '#fc4f30'

plt.axvline(median_grade, color=color, label='Grade Median', linewidth=2)

plt.legend()

plt.title('Student Grade')
plt.xlabel('Grade')
plt.ylabel('Total student')

plt.tight_layout()


x = input_sample_data_01.data['id']
y = input_sample_data_01.data['mas291']
plt.hist(y,bins = 5)
plt.title('bài ca fuckboy')
plt.ylabel('frequency')
plt.xlabel('Score')
plt.show()


k = np.array([0,2.2,4.4,6.6,8.8,10])
mylabels = [0,2.2,4.4,6.6,8.8,10]

plt.pie(k,labels=mylabels,startangle=90)
plt.show()

reports=[]

with open('SAMPLE_DATA_01.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        masv = row['ID']
        mark = row['MAS291']
        reports.append({'masv': masv,
                        'mark': mark})

#Draw by counter marks

distributions = [float(mark['mark']) for mark in reports]
counter = Counter(distributions)
number_of_marks = []
distributions_of_mark = []
for key in counter.keys():
    distributions_of_mark.append(key)
    number_of_marks.append(counter.get(key))

pyplot.barh(number_of_marks,distributions_of_mark,
           color='blue',
           label='Distribution of marks')
pyplot.show()

