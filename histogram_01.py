import csv
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

