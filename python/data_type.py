# Built-inata types
# in programming datatype is an important concept
# varibles can stor data of different types, different types can do different things
# pythonhas the following  data type s built-in b deault, in these categories
# text Type  str
# Numeric Types : int, float, complex
# Sequence Types : list, typle, range
# Mapping type: dict
# Set types set, frozenset
# Boolean type bool
# Binary Types bytes, bytearray,  memoryview
# None  Types:  noeType
#

# Getting  the data  Types
# you can get the dta type of any object by using the `type()` function
#
# example : print the data type of the varibles x
x = 5
print(type(x))

# Setting the data type
# - in python, the data type is set when you assing a value  to a variable

x = "Hello world"  # srt
x = 20  # int
x = 20.5  # float
x = 1j  # comolex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)  # range
x = {"name": "John", "age": 36}  # dict
x = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})  # frozenset
x = True  # bool
x = b"Hello"  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # memooryview
x = None  # NoneType


# Setting the specific data type
# if you want to specify the data type, you can use the following consturecto function

x = str("Hello world")  # str
x = int(20)  # int
x = float(20.5)  # float
x = complex(1j)  # complex
x = list(("apple", "banan", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)  # range
x = dict(name="John", age=27)  # dict
x = set(("apple", "banana", "cherry"))
x = frozenset("apple", "banana", "cherry")  # frozenset
x = bool(5)  # bool
x = bytes(5)  # bool
x = bytearray(5)  # bytearray
x = memoryview((bytes(5)))  # memoryview
