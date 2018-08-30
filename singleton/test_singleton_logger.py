"Test singleton example object."

from singleton_ligger import Logger

obj1 = Logger("File value 1")
 
print("print obj1: ", obj1)
print("---")

obj2 = Logger("File value 2")
print("print obj1: ", obj1)
print("print obj2: ", obj2)