#from collections import deque
import collections as cool
#Lambda stands for anonymous function
#the first x before the semicolons is the parameter, you can have multiple parameters, and a default parameter
jeez = lambda x=2: x * 3
print(jeez())

#the counter function and element function is found in the collections function
#the counter function counts the amount of a certain element is in a list/iterable and prints it in the terminal as a dictionary with key value pairs.
c = cool.Counter(["jackie","fantashia"])
d = cool.Counter(["love", 2, 2, "l", "n", "n", "j", "o"])
print(d)
print(c)
c.elements()

#namedtuple is an method or function found in the collections module that creates a object tuple or just a tuple
#namedtuple requires an object or variable name and key values to pair whatever numbers or other elements or values you wish to add to the variable

g = cool.namedtuple("love", ["j", "p","l"])
print(g(3,4,5))

d = cool.deque("jessica", 4)
d.append(cool.deque("santiago"))
print(d)
#the deque method is found only in the collections module and is used to split every element  in a string into separate indexes in a list variable/iterable.
#the deque method takes one or two parameters the first is a string, the second is a integar
#the second parameter which is a integar in the deque method splits the string starting from the back of the string towards the front of the string.
#and the deque method will only add the elements of the back of the string by whatever number you put in the second parameter.
#if you do not put in a second parameter the deque method will split the whole string into separate indexes