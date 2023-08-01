people = {1: {'name': 'John', 'age': 27, 'sex': 'Male'},
          2: {'name': 'Marie', 'age': 22, 'sex': 'Female'},
          3: {'name': 'Luna', 'age': 24, 'sex': 'Female'}}

def names(people_dict):
    for key, value in people_dict.items():
        if people_dict[key]['age'] > 22:
            print(people_dict[key]['name'])


names(people)