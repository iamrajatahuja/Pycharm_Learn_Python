# pickle module is used for serialization and deserialization of python sequences(lists,dict..)

import pickle
students = {'student1': {'age': False, 'name': 'aul'},
            'student2': {'age': True, 'name': 'Rudffdfd'},
            'student3': {'age': True, 'name': 'Xavioooo'}}

print(students, type(students))

#Serialize
with open('practice.bin', 'wb') as fh:
    pickle.dump(students, fh)
    """for student in students:
        pickle.dump(students[student], fh)"""

#Deserialize
with open('practice.bin', 'rb') as fh:
    while True:
        try:
            data = pickle.load(fh)
            print(data,type(data))
        except EOFError:
            print("Done")
            break
print(data)



