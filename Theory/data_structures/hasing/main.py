# Hashing: Gives fast searching.

# Linear search : O(n) -> check each items
# binary search on sorted array: O(log(n)) -> When output multiplies than operations get added thus log n.

# Hashing: O(1) -> Constant Time.
# Each item in the array is stored in a particular way, in a fixed index
# which is determined through a hash function which is custom and made by us.
# Thus, when we want to search an item we run it through that function and get the index value
# and directly check at the index. If the ele we want to search != the value at that index, it means ele doesn't exist.
# NOTE: Arr[index] is constant as it fetches from addr + index*memory of each element. This is used in hashing.

# Hashing Function : Can we any custom-made function with the least collisions and best performance.
# Ex. (i % size) -> mostly so that total size of table after hashing = total no.of elements needed to put in the array.
# Thus, not much space is wasted. As the index can only range between (0 <= index < size)

# ** ASCII TABLE helps when words are involved : https://www.ascii-code.com/
# Convert character to ASCII value
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")  # Output: The ASCII value of 'A' is 65

# Convert ASCII value to character
ascii_value = 66
char = chr(ascii_value)
print(f"The character with ASCII value {ascii_value} is '{char}'")  # Output: The character with ASCII value 66 is 'B'

# Hash Value : The o/p of hashing function and also index at which an element is stored in an arr.
# collisions : When multiple items have same hash value and need to be stored at same location, it creates collision.
# Our aim is to write a hash func with the least collisions.
# To solve collisions:
# Closed addressing technique: Chaining
# Open addressing technique: Linear probing, Quadratic probing.: The new item can be put to new address due to collision

# Closed addressing technique: Chaining -> Even after collision the new item should be at the same index.
# In chaining : We create a node arr. Each node initially until collision, the next will point to null.
# In Case of collision, at that index, a ll type will be created with new item at node.next of the already existing item


