import csv
import pandas as pd
from matplotlib import pyplot as plt
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

data = pd.read_csv('data.csv')
ids = data['ID']
grades = data['Grade']

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

plt.show()
