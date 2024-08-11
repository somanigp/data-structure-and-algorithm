# Linear Probing and Quadratic Probing
from typing import Any


# Creating Dict class using hashing in python.
class Dictionary:
    def __init__(self, size: int):
        self.size = size
        self.slots = [None] * self.size  # For storing keys  # ** arr of len=size and all elements are None.
        self.data = [None] * self.size  # For storing data at the same index as keys.

    def __setitem__(self, key, value):  # NOTE: ***MAGIC METHOD
        # Can use dict1[0] = "Welcome". Type of way to put key and value
        self.put(key, value)

    def put(self, key: Any, value: Any):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:  # In case of updating the dictionary
                self.data[hash_value] = value  # Updating the key with new value
            else:  # In case of collision with another key already in place
                new_hash_value = self.rehash_function_linear(hash_value)
                while (self.slots[new_hash_value] is not None) and (self.slots[new_hash_value] != key):
                    # Empty or the same key exists somewhere forward.  # NOTE: Used AND**. As it should exit if any one
                    # is false.
                    new_hash_value = self.rehash_function_linear(new_hash_value)  # Incrementing hash value linearly

                if self.slots[new_hash_value] is None:  # Empty
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                else:  # The same key exists somewhere forward.
                    self.data[new_hash_value] = value

    def hash_function(self, key: Any):  # Need hash value for key only and in dict we get items from key and value
        # has same hash value as key, i.e same index to corresponding key.
        # NOTE: ** print(-5 % 2)  # Result is +1, positive.
        return abs(hash(key)) % self.size  # abs makes all positive

    def rehash_function_linear(self, old_hash_value):
        return (old_hash_value + 1) % self.size  # Linear Probing : old_hash_value + 1

    def get(self, key):
        # To return corresponding value
        start_position = self.hash_function(key)  # So to check that it has again returned to initial position, if it
        # has, it means key not found.
        # NOTE: ** Other condition for key not existing is if the key at next index is NONE. Meaning in linear probing,
        # if key did exist it should have been there instead of None as you add key at next available space.
        current_position = start_position
        while (self.slots[current_position] != key) and (self.slots[current_position] is not None):
            current_position = self.rehash_function_linear(current_position)  # Updating the key linearly.
            if current_position == start_position:  # If returned to start then key doesn't exist
                raise ValueError("Key doesn't exist")
        if self.slots[current_position] == key:  # If key exists and return value
            return self.data[current_position]
        else:  # If None encountered first then key doesn't exist
            raise ValueError("Key doesn't exist")

    def __getitem__(self, item):  # MAGIC METHOD
        # x[key] is enabled through this. ** NOTE.
        self.get(item)


# dict.update(other_dict) : This method updates the dictionary with the key-value pairs from another dictionary or an
# iterable of key-value pairs.

# hash() function in python : returns the same int value if input is int.
# calculates hash for strings and other types too. The hash value is const for same immutable item.
# Thus helps in creating hash functions.
# For mutable type like: list, set , etc. it gives error.

d1 = Dictionary(3)
d1["java"] = 100
d1["python"] = 217
d1["php"] = 0
print(d1.slots, d1.data)

d1["java"] = 126
print(d1.slots, d1.data)
# d1["c++"] = 10  # This will fail as we have not added a functionality to increase size to add more items i.e make
# dict dynamic. We have also not added functionality to return error or None is item not found in fixed length dict.
print(d1.get("java"))
print(d1.get("C"))  # Key doesn't exist
