#JSON vs Python Dictionary: Only "" double quotes used in JSON and boolean data is in small case true
#JSON is used for API and data storage / interchange of data
#json is a module in Python

import json

students = {'student1': {'age': False, 'name': 'Raul'},
            'student2': {'age': False, 'name': 'Rudffdfd'},
            'student3': {'age': True, 'name': 'Ravioooo'}}
print(students, type(students))

#dump() method to add data in json file(Serialization)

with open('practice.json', 'w') as fh:
    json.dump(students, fh, indent=4) #indent is just for decorating

#load() to read the json and return dict (Deserialization)
with open('practice.json', 'r') as fh:
    data = json.load(fh)
print(data, type(data))

#update() to update and add new data
data.update(students)
with open('practice.json', 'w') as fh:
    json.dump(students, fh, indent=4)