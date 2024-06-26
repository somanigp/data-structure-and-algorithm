# Array: Linear DS used to store multiple items of same type in continuous memory location
# Disadvantage: fixed size in java, c++. and thus memory wastage if you assume large memory. -> tackled by dynamic array
#               Homogeneous data means lack of flexibility. -> tackled by referential array

# Arrays are of 2 types : call by value and call by reference
# Call by value : values stored inside an array in a continuous memory location
# Call by reference (referential array) : location of values are stored in the array in a continuous memory location. The actual values can all be on different locations. This can help make array more flexible, can store str and int together. This is because the array has only location of values thus is still homogeneous. Drawback : speed slow and extra memory
# Python List is referential array.


# Static Array: fixed size array. This is always the case in memory
# Dynamic Array: Array that can be resized. Made out of static arrays only. When a static arr is full and you need to input more values than you create anothern static array with double size and copy the contents of first array. Python list is dynamic array.

import sys
import ctypes  # create and manipulate C data types in Python
from typing import Any

L = []

for i in range(100):  # Proof/Working of dynamic array. getsizeof -> gives size in memory. ** Different for each server.
    size_of_L = sys.getsizeof(L)
    # print(f"Length of L is {len(L)} and size of L in bytes is {size_of_L}")  # Uncomment this to see the working of dynamic array
    L.append(i)

# Creating a dynamic array/python list using ctypes
class MeraList:
    
    def __init__(self):  # Constructor
        self.size = 1  # capacity of the array. Max no of elements possible.
        self.n = 0  # No of values in the array. n is the index at which the next element will be added. n=0 means empty array and the 1st element will be stored at index 0.
        self.A = self.make_array(self.size)  # returns a array of capacity which is passed.  # A is the referential array.
        
    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()  # returns a C type array with size = capacity. Also this array can have empty elements.

    def __len__(self):  # MAGIC MWTHOD** NOTE: this function is called when len() is called on the object. Thus the class of that object needs to have this __len__(self) function.
        return self.n  # Returns the no. of values present in the list
    
    def append(self, item: Any):  # Creating append method, item can be any object
        if self.size == self.n:  # If at max capacity and no more items can be added
            self._resize(2 * self.size)
        self.A[self.n] = item  # Will append at n, as n is the space left
        self.n += 1  # Increasing no. of items
        
    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)
        for i in range(self.n):  # Range ends at self.n - 1
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity
        
    def __str__(self) -> str:  # MAGIC METHOD** NOTE: 
        pass

    # def __getitem__(self, i):
    #     if not 0 <= i < self.size:
    #         return IndexError('Index is out of bounds')
    #     return self.A[i]



L = MeraList()
print(type(L), L, len(L))
L.append(1)
L.append(True)
L.append("Hello")
L.append(34.56)
print(len(L))

    