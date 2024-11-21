import json
import csv 
with open('student_data.csv', mode='rt') as csv_file:
        csv_data = list(csv.DictReader(csv_file))
        json_data = {"students": csv_data}
with open('student_data.json', mode='w') as json_file:
    json.dump(json_data, json_file)