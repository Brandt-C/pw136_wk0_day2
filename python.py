# This is a comment!
# this is the ONLY symbol in python for comments whether multi or single line BUT you can also put it IN a line of code
print('hello world!') #This is super cliche!!!!

#to-do, explaining a line of code

#DATA-TYPES:
    # Numbers:
        # integer, float   (and complex)
    # String
    # List **** also tuple and range
    # Dictionaries
    # boolean
    # NoneType

# MATH

# add   +
print( 5 + 5)

# subtract   -
print(5-5)

#multiply   *
print(type(5 * 5))

#divide   /
print(5 / 5)
print(type(5 / 5))

# floor divide //
print(25 // 5)
print(type(28 // 5))

#Side-bar   -type-casting/converting values
print('Side-bar on converting types:\n')
long_float = int(56.9087239847)   #56.9087239847   --->   56
print(long_float)
print(type(str(long_float)))   #56  -->  "56"  -->  get the type
print(56 == '56')


print('\nmodulo:')
# modulo    %   --> gives us the remainder
print(25 % 5)
print(28 % 5)

# to figure oddd/even:

print(24 % 2 == 0) # is this even?
print(27 % 2 == 0) # is this even?

print(24 % 2 == 1) # is this odd?
print(27 % 2 == 1) # is this odd?

print(24 % 2 != 0) # is this odd?
print(27 % 2 != 0) # is this odd?

#side-bar   equals. . . 

# comparison operators:
# ==   equal?

# >   
# <
# <=
# >=

# !=  not equal?

# but what about = ???  This is assignment!
# x = 56

#exponent  **  --> to that power
print(5 ** 5)

print('\nOn to Strings!')
#Strings!
#strings are in either single or double-quotes (whatch yourself)
# strings are . . .   ordered, iterable, and immuteable!
st1 = 'This is a string'
st2 = "So's this"
st3 = 'Other chars too! 23 3$%3 34^ 2^234 2#$%^$&#'
st4 = "that's cool"
st5 = 'let\'s talk about escape chars!'
st6 = '12345'
st7 = 'this is a string'
st8 = '\nExample!!!!'

print(len(st6))
print(st6[0])
print(st5[0])
print(st4[0])
# print(st4[986])   out of range err

print(st3[37])
print(st3[-2])
print(st5)

#concatenation
# we can add strings (both variables and literals) together!
print(st1 + st2 + st3)
print(st1 + '. ' + st2 + '. ' + st3 +'. No point  but I decided to add this too!')

st9 = st5 + st4 + 'why not?'
print(st9)


print('\nF-strings')
# interpolation  - what about those numbers?  those python variables?
# f-strings!
# Throw an f in front of your quotes and you can put python things into curly braces!

student1 = 'Bethany'

fst1 = f"This is my f-string and here's a number from above : {5 + 5 -4 ** 4}"
print(fst1)
print(f"in a print statement: {456}")
print(f"This is a great student: {student1}")

print('this is a number using concatenation:' + str(76+934875))



#side-bar. . .  re-definition
# str = 'lkajs;dlfkj'
# print(str(9875))
    # Don't re-define built-ins!

#Functions vs methods:
#syntax is your first clue:    function_name()   vs   data_type.method()
# methods work on a particular data type and functions can work on many

print(fst1.lower().upper())
print('example'.upper())

# Lists!
# lists are kinda like a container. . .  they can hold just about any data type. . .
# lists are ordered, iterable, and muteable, and dynamic
# syntax . ..  []     
# #synonomous with array
print('\nOn to lists:')

my_list = []
num_list = [1, 2, 3, 4, 5]
st_list = ['one', 'two', 'three', 'four', 'five']
confused_list = [1, 'two', 3.0, 4, [], True, {'This is a dictionary key': 'Value'}, None]

print(st_list[2])
print(st_list[-1])
st_list[2] = 'STRING'
print(st_list)
print(confused_list)

print('\nconfusing nested example:')
nested_list = [1, 1, 2, 'twenty', [0, 'one', [['x']]]]
nested_list2 = [
    'string',
    [
        1,
        2,
        3,
        [
            [
                'value'
             ]
        ]
    ]
]

print(nested_list[4])
print(nested_list[4][2])
print(nested_list[4][2][0])
print(nested_list[4][2][0][0])

print(nested_list2[1][3][0][0])
print(nested_list2)

print('\nList methods:')
emp_list = []

#append method
# list.append()
# adds to the end of the list

emp_list.append('zero')
emp_list.append('one')
print(emp_list)
emp_list.append('two')
print(emp_list.append('three'))
print(emp_list)

# pop method
# list.pop()
# removes the last item from the list. . . BUT
# this RETURNS a value so we can use it, ALSO there is an optional parameter to specify position

name = emp_list.pop()
print(emp_list)
print(name)
emp_list.pop(1)
print(emp_list)

print('\n remove method:')
# remove
# list.remove(value)
# removes a value from a list. . . specifically the FIRST occurence
emp_list.remove('zero')
print(emp_list)
emp_list.append('two')
emp_list.append('two')
emp_list.append('two')
print(emp_list)
emp_list.remove('two')
print(emp_list)

# loops
# 3 types of loops:
#  for loop,  the index loop, and the while loop

# the for loop
#syntax --->    for item in collection:
                    #code block
# or            for word in words:

print('\nLoops:')
strings = ['one', 'two', 'three', 'four', 'five']

for string in strings:
    print(string.upper())
print(strings)

    
# Side-bar  -- Range
# Range() is a generator. . . it has 3 parameters, START, STOP, STEP
# The stop is the only one required!  the start defaults to 0 and the step defaults to one, UNLESS otherwise specifcied.
# for x in range(5):
#     print(x)

for x in range(5, 11):
    print(x)

for x in range(1, 20, 2):
    print(x)

for x in range(21, 5, -2):
    print(x)

print('\nIndex loop')
strings = ['one', 'two', 'three', 'four', 'five']
# index loop
# for i in range(len(iterable)):
    #code block
for i in range(len(strings)):
    print(i, strings[i])
    strings[i] = 'NOTHING'
print(strings)



#side-bar 
# incrementing/decrementing

a_num = 56

print(a_num + 44)
print(a_num)
a_num = a_num + 44
print(a_num)
a_num += 100
print(a_num)

a_num -= 100
a_num *= 5
print(a_num)

# while loop:
# loop based on a conditional:
# while this condition is true:
    #do this
# Don't create infinite loops!

count = 0
while count < 5:
    print(strings[count])
    count += 1

while True:
    print('only once!')
    break



#side-bar for tomorrow/ truthy/falsy

print('\nTruthy/falsey. . . ')
# some things evaluate as True or False in python:
# falsy examples:   ''    []     0   
# truthy exp:        'anything'    ['anything']   1
print(bool([234]))



#Conditionals:
#  if  <conditional>:
    #codeblock to execute

if 5 < 1:
    print('duh')

# chaining conditionals, but we can use 
# elif <condtional>:
#or
# else:
#The difference between using any number of ifs vs elif/else is that we're evaluating the same condition
#which means that ONLY one of those codeblocks will fire

age = 14
height = 8763

# if age < 18:
#     print('kid')
# if age >= 18:
#     print('adult')
# if age > 65:
#     print('senior')

if age < 18:
    print('kid')
elif age > 65:
    print('senior')
else:
    print('adult')



if age < 18:
    print('kid')
elif age > 17 and age < 65:
    print('adult')
else:
    print('senior')

# Truth-tree:
# for and
# T & T = T
# T & F = F
# F & F = F


#for or
# T or T = T
# T or F = T
# F or F =  F



if age > 17 or height > 567:
    print('at least they\'re tall!')


#Functions
# Because we don't want to type the same thing over and over
# syntax -->    
# def func_name(<parameter>, <another_parameter>):
    #Codeblock to execute

def add(num1, num2):
    print(num1 + num2)


add(5.0, 5)
print(add(10, 10))

def mult(a, b):
    return a * b
print(mult(10, 10))

add(mult(10, 10), 50)
# (mult(add(5, 5), 4))

def namer(f_name):
    print(f"HELLLLO {f_name.title()}")

namer('parker')
namer('mike')
namer('jorge')

# membership checks
# in
for letter in ';lkajsdf;lk':
    if letter == 'j':
        print(f"found {letter}")

print('j' in 'lskdfj')
n_list = [ 1, 2, 3, 4, 5, 6]
print(5 in n_list)
name_list = ['parker', 'mike', 'jorge']
for name in name_list:
    print(name.upper())
    namer(name)


































