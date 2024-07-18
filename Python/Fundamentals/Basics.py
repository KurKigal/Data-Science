#GENERAL
'''
Python is case sensitive 
Python index starts from 0
Python uses whitespace (tabs or spaces) to indent code instead of using braces
'''

#HELP

#Help Home Page: 
help()

#Function Help:  
help(str.replace)

#Module Help:    
help(re)


#MODULE

#Python module is simply a ".py" file


#List Module Contents:       
dir(module1)

#Load Module:                
import module1

#Call Function from Module:  
module1.func1()   


#SCALAR TYPES

#Check Data Type:
variable = 1    
type(variable)

'''
int/long: Large int automatically converts to long
float: 64 bits, there is no "double" type
bool: True or False
str: ASCII valued in Python 2.x and Unicode in Python 3
None
'''


#DATA STRUCTURES

#LISTS

#Make a list:
bikes = ['trek', 'redline', 'giant']

#Get the first item:
first_bike = bikes[0]

#Get the last item:
last_bike = bikes[-1]

#Add an item to end of list:
bikes.append('new_bike')

#Insert to Specific Position
bikes.insert(position, 'new_bike') 

#Remove first value from list:
bikes.remove('trek')



#LIST TYPES

#TUPLE

'''
One dimensional, fixed-length, immutable sequence of Python objects of ANY type.
'''

#Make a tuple list:
dimensions = (1920, 1080)


#DICTINORY (HASH MAP)


#Make a Dict:
dict1 = {'key1': 'value1', 2:[3,2]}

#Create Dict from Sequence:
dict(zip(keyList, valueList))

#Get/Set/Insert Element:
dict1['key1'] = 'newValue'

#Get with Default Value:
dict1.get('key1', defaultValue)  # 'get()' by default (aka no 'defaultValue') will return 'None' if the key does not exist.

#Check if Key Exists:
'key1' in dict1

#Delete Element:
del dict1['key1']

#Get Key/Value List:
dict1.values()
dict1.keys() 
    
#Returns the lists of keys and values in the same order. However, the order is not any particular order, aka it is most likely not sorted.

#Update Values:
dict1.update(dict2) #dict1 values are replaced by dict2


#SETS

'''
#A set is an unordered collection of UNIQUE elements. (dict but keys only)

Make a set:
set([3,6,3]) or set{3,6,3}

Test Subset:
set1.issubset(set2)

Test Superset
set1.issuperset(set2)


Set operations:
Union(aka 'or'):                    set1 | set2
Intesection(aka 'and')              set1 & set2
Diffrence                           set1 - set2
Symmetric Diffrence(aka 'xor')      set1 ^ set2
'''


#IF STATEMENTS

'''
equals x == 42
not equal x != 42
greater than x > 42
or equal to x >= 42
less than x < 42
or equal to x <= 42
'''

'trek' in bikes
'surly' not in bikes

game_active = True
can_edit = False

if age >= 18:
    print("You can vote!")

if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15


#WHILE LOOPS

current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1


#Letting the user choose when to quit        
msg = ''
while msg != 'quit':
    msg = input("What's your message? ")
    print(msg)


#FOR

'''
#In Python, the for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence.

for item in sequence:
    # do something with item

    
range()
    The range() function generates a sequence of numbers, which is often used with for loops.

    for i in range(5):
    print(i) 
    
    #Output: 0 1 2 3 4 

for Loop with else
    for i in range(3):
        print(i)
    else:
        print("Loop finished")

Breaking Out of a for Loop
    for i in range(5):
        if i == 3:
        break
        print(i)

Continuing to the Next Iteration
    for i in range(5):
        if i == 3:
            continue
        print(i)
'''

#FUNCTION


#A simple function

def greet_user():
    print("Hello!")

greet_user()

    
#Passing an argument 
    
def greet_user(username):
    print("Hello, " + username + "!")

greet_user('jesse')

#Default values for parameters

def make_pizza(topping='bacon'):
    print("Have a " + topping + " pizza!")

make_pizza()
make_pizza('pepperoni')

#Returning a value

def add_numbers(x, y):
    return x + y

sum = add_numbers(3, 5)
print(sum)
     
