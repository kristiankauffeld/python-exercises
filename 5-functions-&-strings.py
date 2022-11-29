#TASK 1
#Write a normal function that accepts another function as an argument. 
# Output the result of that function in your normal function.
def greet(func):
    print(func('alice'))

#TASK 2
#Call your "normal" function by passing a lambda function 
# - which performs any operation of your choice - as an argument.
greet(lambda data: data.upper())

#TASK 3
#Tweak your normal function by allowing an infinite amount of arguments on which
#your lambda function will be executed.
def greet2(func, *args):
    for arg in args:
        print(func(arg))

greet2(lambda data: data.upper(), 'bob', 'charlie')

#TASK 4
#Format the output of your "normal" function such that the data look nice
#and are centered in a 20 character column
def greet3(func, *args):
    for arg in args:
        print('result: {:^20}'.format(func(arg)))

greet3(lambda data: data.upper(), 'bob', 'charlie')
