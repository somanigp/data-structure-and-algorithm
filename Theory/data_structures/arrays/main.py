# Array: Linear DS used to store multiple items of same type in continuous memory location
# Disadvantage: fixed size in java, c++. and thus memory wastage if you assume large memory. -> tackled by dynamic array
#               Homogeneous data means lack of flexibility. -> tackled by referential array

# Arrays are of 2 types : call by value and call by reference
# Call by value : values stored inside an array in a continuous memory location
# Call by reference (referential array) : location of values are stored in the array in a continuous memory location.
# The actual values can all be on different locations. This can help make array more flexible, can store str and
# int together. This is because the array has only
# location of values thus is still homogeneous. Drawback : speed slow and extra memory
# Python List is referential array.


# Static Array: fixed size array. This is always the case in memory
# Dynamic Array: Array that can be resized. Made out of static arrays only. When a static arr is full and you need
# to input more values than you create another.
# static array with double size and copy the contents of first array. Python list is dynamic array.

import sys
import ctypes  # create and manipulate C data types in Python
from typing import Any

L = []

for i in range(100):  # Proof/Working of dynamic array. getsizeof -> gives size in memory. ** Different for each server.
    size_of_L = sys.getsizeof(L)
    # print(f"Length of L is {len(L)} and size of L in bytes is {size_of_L}")  # Uncomment this to see the working
    # of dynamic array
    L.append(i)


# Creating a dynamic array/python list using ctypes
def make_array(capacity):
    return (capacity * ctypes.py_object)()  # returns a C type array with size = capacity. Also this array can have
    # empty elements.


class MeraList:

    def __init__(self):  # Constructor
        self.size = 1  # capacity of the array. Max no of elements possible.
        self.n = 0  # No of values in the array. n is the index at which the next element will be added. n=0 means
        # empty array and the 1st element will be stored at index 0.
        self.A = make_array(self.size)  # returns an array of capacity which is passed.
        # A is the referential array.

    def __len__(self) -> int:  # MAGIC METHOD** NOTE: this function is called when len() is called on the object.
        # Thus the class of that object needs to have this __len__(self) function.
        return self.n  # Returns the no. of values present in the list

    def append(self, item: Any):  # Creating append method, item can be any object
        if self.size == self.n:  # If at max capacity and no more items can be added
            self._resize(2 * self.size)
        self.A[self.n] = item  # Will append at n, as n is the space left
        self.n += 1  # Increasing no. of items

    def _resize(self, new_capacity):
        B = make_array(new_capacity)
        for i in range(self.n):  # Range ends at self.n - 1
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity

    def __str__(self) -> str:  # MAGIC METHOD** NOTE: Override the str method, thus will o/p this when
        # print(class object) is used.
        # Without this it returns <__main__.MeraList object at 0x0000026667407EF0> for a class object.
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ','  # str(Any) -> type conversion to string. It helps print the object.
        return '[' + result[:-1] + ']'  # l[:-1] From 0 to last element, note thus this excludes the last element.

    # TypeError : 'MeraList' object is not subscriptable --> if we not enable l[0] indexing.
    def __getitem__(self, index: int) -> Any:  # MAGIC METHOD** NOTE: This allows us to use indexing on the object.
        # Thus will give o/p when l[0] is used. Makes object subscriptable. Triggers on [index] in front of object.
        if not 0 <= index < self.n:  # (0 <= i < self.n) is an expression. if not (true/false).
            # NOTE: n here as n is no. of elements actually present and <n excludes n, which index is yet to be filled.
            raise IndexError('Index is out of bounds')
            # if you use : return IndexError('Index is out of bounds').
            # Then it won't break the program but print the error.
        return self.A[index]  # Return element at that index

    def pop(self) -> Any:
        """Will remove the last element from the list and return it"""
        if self.n == 0:  # If n=0, ie no element in the list
            raise IndexError('pop from empty list')
        item = self.A[self.n - 1]  # n is no of element in the list. Thus index of last element n-1.
        self.A[self.n - 1] = None  # Element pos to None which we are removing.
        self.n -= 1  # Deceasing no of elements in array by 1.
        return item

    def clear(self):
        """Removes all the elements from the list"""
        for index in range(self.n):  # Iterate over all indexes
            self.A[index] = None  # All elements set to None
        self.n = 0  # No of elements in the list to be 0
        self.size = 1  # Size of the array to be 1. As now, it is empty. During the addition of second element the
        # memory of self.A will truly change saving us space.

    def index(self, item: Any) -> Any:
        """Finds the first occurrence of item in the list."""
        for index in range(self.n):
            if self.A[index] == item:
                return index
        raise ValueError(f'{item} not in list')

    def insert(self, index: int, value: Any):
        """inserts an element at the position, and shifts all the rest to right"""
        if not 0 <= index <= self.n:
            raise IndexError("Index is out of bounds")
        if self.n == self.size:  # At full capacity, thus add space to add element
            self._resize(2*self.size)
        # NOTE: Below for loop won't execute if index = n, ie when inserting the value at the end.
        for i in range(self.n, index, -1):  # n is included, last element is stored at n-1 which needs to shift to n.
            self.A[i] = self.A[i-1]  # Shifting each element to right from the end.
        self.A[index] = value
        self.n += 1  # Increase no. of elements

    def remove(self, value: Any):
        """removes the first occurrence of that element"""
        pos = self.index(value)
        self.__delitem__(pos)
        # for index in range(self.n):
        #     if self.A[index] == value:
        #         self.__delitem__(index)
        #         break

    # delete : deletes the element at that pos. del l[2]
    def __delitem__(self, key):  # \n works inside """ """.
        """Delete the element at pos=key.\n
        Eg: del l[1]"""
        if not 0 <= key < self.n:
            raise IndexError("Index is out of bounds")
        for index in range(key, self.n-1):  # Shift all elements to left and delete the last place.
            # self.n-1 as we want second last ele (self.n-2) to be last ele (self.n-1).
            self.A[index] = self.A[index+1]
        self.A[self.n-1] = None
        self.n -= 1  # Decrease the length by 1


L = MeraList()
print(type(L), L, len(L))
L.append(1)
L.append(True)
L.append("Hello")
L.append(34.56)
L.append({1: "hello"})
print(len(L), L)
print(L[0], L[1])
# print(L[100])
print(L.pop())
print(len(L))
L.clear()
print(len(L), L)
L.append(1)
L.append(2)
L.append(3)
print(L.index(2))
print(L)
L.insert(index=0, value=10)
print(L)
L.insert(4, 22)
print(L)
del L[1]
print(L)
del L[3]
print(L)
L.append(100)
L.append(50)
L.append(2)
print(L)
L.remove(2)
L.remove(50)
print(L)

is_list = ["1", "2", "3"]
l1 = list()  # Can initialize list like this too.
