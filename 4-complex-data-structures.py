#TASK 1
#Create a list of "person" dictionaries with a name, age and list of hobbies for each person.
persons = [
    {
        'name': 'Alice',
        'age': 25, 
        'hobbies': ['hacking', 'cooking']
    },
    {
        'name': 'Bob',
        'age': 30, 
        'hobbies': ['programming', 'exercise']
    },
        {
        'name': 'Charlie',
        'age': 15, 
        'hobbies': ['trolling', 'gaming']
    }
]


#TASK 2
#Use a list comprehension to convert this list of persons into a list of names (of the persons).
list_of_persons = [person['name'] for person in persons]
print(list_of_persons)


#TASK 3
#Use a list comprehension to check whether all persons are older than 20.
if all([person['age'] > 20 for person in persons]):
    print('All persons are older than 20')
else:
    print('Everyone is not over 20')


#TASK 4:
#Copy the person list such that you can safely edit the name of the first person (without changing the original list).
copied_persons_list = persons[:]

#copied_persons_list [0]['name'] = 'Mallory' #This only creates a shallow copy

dict_copy = copied_persons_list[0].copy() #This creates a deep copy.
dict_copy['name'] = 'Mallory'
copied_persons_list[0] = dict_copy

print(persons[0]['name'])
print(copied_persons_list[0]['name'])


#TASK 5
#Unpack the persons of the original list into different variables and output these variables
person1, person2, person3 = persons
print(person1)
print(person2)
print(person3)
