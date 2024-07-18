#Enumerate

'''
The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
This is useful for obtaining an indexed list from an iterable. The first parameter is the iterable, and the second (optional) parameter is the starting index (default is 0). 
''' 

example_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(example_list, start=1):
    print(index, value)  # Output: 1 apple, 2 banana, 3 cherry


#Zip

''' 
The zip() function takes two or more iterables (e.g., lists, tuples) and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.
This is useful for combining two lists element-wise. If the iterables are of uneven length, zip stops when the shortest iterable is exhausted.
''' 

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

#List Comprehensions

''' 
List comprehensions provide a concise way to create lists. 
Common applications include creating a new listby applying some expression to each element of an existing list or filtering elements of a list.
'''

squared = [x**2 for x in range(10)]  # Creates a list of squares of numbers from 0 to 9
print(squared)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Lambda Expressions

''' 
Lambda expressions are small anonymous functions defined with the lambda keyword. 
They can have any numberof arguments but only one expression. They are syntactically restricted to a single expression.
This is useful for creating short functions without needing to formally define them.
'''

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

#Map

''' 
The map() function applies a given function to all items in an iterable (e.g., list) and returns a map object(an iterator).
You can convert the result to a list or another iterable type if needed.
This is useful for applying a transformation to each element in a list. 
'''
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16]

#Filter

'''
The filter() function constructs an iterator from elements of an iterable for which a function returns true.
This is useful for filtering elements in a list based on a condition.
''' 
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

#Global and Local Variable

''' 
# Global variables are accessible throughout the entire program, while local variables are only accessible
# within the function they are declared in. You can use the global keyword to modify a global variable inside a function.
''' 

x = 'global'
def foo():
    global x
    x = 'local'
    print(x)  # Output: local
foo()
print(x)  # Output: local

#Error Handling

''' 
Error handling in Python is done with try and except blocks. 
You can catch specific exceptions or use a general except block to catch all exceptions. 
This is useful for managing exceptions and preventing your program from crashing.
''' 

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!

# You can also use finally to execute code regardless of whether an exception occurred or not.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always be executed.")  # Output: This will always be executed.
