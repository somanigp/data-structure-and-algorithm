from typing import Any, Union
# Importing LinkedList and Node classes
# from Theory.data_structures.linked_list.single_linked_list_class import LinkedList, Node


class Node:  # For purpose of created Dictionary through chaining, ie closed addressing.
    def __init__(self, key: Any, value: Any):  # Both key and value stored in single node.
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        """Initialize ll object."""
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def __str__(self) -> str:
        pointer = self.head
        result: str = ''
        if pointer is None:
            return result
        while pointer.next is not None:
            result += str(pointer.key) + ' : ' + str(pointer.value) + ', '
            pointer = pointer.next
        result += str(pointer.key) + ' : ' + str(pointer.value)
        return result

    def insert_tail(self, key: Any, value: Any):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
        self.n += 1

    def clear(self):
        """Make LL empty"""
        self.head = None
        self.n = 0

    def delete_from_head(self):
        """Delete the first element from start"""
        if self.head is None:
            raise ValueError("The list is empty")
        self.head = self.head.next
        self.n -= 1

    def delete_by_key(self, value: Any):
        # Here Value will be the 'key' provided to search by.
        """Deletes the Node/Item which has key=value"""
        pointer = self.head

        # Empty LL
        if pointer is None:
            raise ValueError("LL is empty")

        # Only one item in the LL
        if pointer.next is None:
            if pointer.key == value:
                return self.delete_from_head()
            else:
                raise ValueError("Value not found")

        # When LL size is >= 2.
        if pointer.key == value:  # Checking if first element matches
            return self.delete_from_head()
        # Need to stop at Node before the node containing the data=value
        while pointer.next.key != value:
            # If no data found which is = to value and there is nothing to delete
            if pointer.next.next is None:
                raise ValueError("Value not found")
            pointer = pointer.next
        pointer.next = pointer.next.next
        self.n -= 1

    def search_by_key(self, value: Any) -> int:  # Index
        """Returns the index of the key provided"""
        pointer = self.head
        index = 0

        # Empty LL
        if pointer is None:
            # raise ValueError("LL is empty")
            return -1
        # If pointer node data=value then returns the index of the pointer
        while pointer.key != value:
            if pointer.next is None:
                return -1  # If value not found.
            pointer = pointer.next
            # Index of current pointer updated.
            index += 1
        return index

    def change_value_at_index(self, index: int, value: Any):
        """index should exist, changes the "value" attribute of Node at that index."""
        pointer: Union[None, Node] = self.head
        for _ in range(index):  # Directly goes to the Node at index.
            pointer = pointer.next
        pointer.value = value

    def node_at_index(self, index: int):
        """index should exist, changes the "value" attribute of Node at that index."""
        pointer: Union[None, Node] = self.head
        for _ in range(index):  # Directly goes to the Node at index.
            pointer = pointer.next
        return pointer


# In closed chaining it's an Array of LL which is used ie each item is a LL itself. So all elements initially will be
# empty ll. Note : Head of empty ll points to None.
# NOTES: In case of collision, add from tail and not head, head is the first element at that spot and will not change.
# NOTES: Delete will happen through value. Not tail or head.
# NOTES: In one node both key and value will be stored. So no need for 2 lists.
def make_array(capacity: int) -> list:
    return [LinkedList() for _ in range(capacity)]  # Array of LL. [LinkedList()] * capacity. 3 Objects are created here
    # return_list = []
    # for _ in range(capacity):
    #     return_list.append(LinkedList())
    # return return_list


# NOTE: **
# print([LinkedList()] * 3)  # This is WRONG. As here the same object is duplication and put thrice in one list.
# No three objects are created. *** Thus, change to one will reflect to others too.
# Change to an object reflects everywhere, where that object is used.

# print(make_array(3))  # [<__main__.LinkedList object at 0x000001F09D05E1E0>,
# <__main__.LinkedList object at 0x000001F09D05E210>, <__main__.LinkedList object at 0x000001F09D05F8F0>]
# NOTE : LL class has __str__ defined still its object in list will be shown like this.
class Dictionary:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0  # No of key-value pair in the dictionary.
        # NOTE: In chaining it's an array of ll, and each linked list is known as a bucket.
        # Thus, an array of bucket is buckets. So each item inside buckets is a bucket.
        self.buckets: list[LinkedList] = make_array(self.capacity)
        # list[LinkedList]: This is the crucial part. It tells us that the list self.buckets will
        # hold objects of the LinkedList class.

    def __setitem__(self, key: Any, value: Any):
        self.put(key, value)

    def put(self, key: Any, value: Any):
        # bucket_index: the bucket no. in which this key-value node will go.
        bucket_index = self.hash_function(key)

        # Check if key already exists in that bucket.
        node_index = self.buckets[bucket_index].search_by_key(key)
        if node_index == -1:  # If the key doesn't exist
            self.buckets[bucket_index].insert_tail(key, value)
            self.size += 1

            # Load Factor/lambda = size/capacity.
            # Ex: If lf/lambda >= 2, rehash -> increase capacity by *2.
            if self.size/self.capacity >= 2:
                self.rehash()

        else:  # If the key already exists
            self.buckets[bucket_index].change_value_at_index(node_index, value)

    def rehash(self):
        # The main reason to use hashing was that the order of growth should be close to O(1).
        # Thus if a lot of elements go into one single linkedlist, and we get close to order of O(n). We need to reduce
        # that and one way is through rehashing.
        # Thus, in this case only we are deciding if lf >= 2. We double the array size to reduce lf.
        self.capacity = 2 * self.capacity  # A
        self.size = 0  # B
        old_buckets = self.buckets
        self.buckets: list[LinkedList] = make_array(self.capacity)  # C
        # Creating conditions A, B and C so that we are at initial condition of dict with new capacity.
        # *** Need to put items of tha old_buckets into new buckets, by recalculation hash for each element again.
        for ll in old_buckets:
            for j in range(len(ll)):  # To access all the index available in that ll.
                new_node = ll.node_at_index(j)
                # Putting existing key-value pairs in new dict.
                self.put(new_node.key, new_node.value)  # NOTE this is for adding in new dict.

    def hash_function(self, key: Any):
        # Deterministic Hashing: This code implements a simple deterministic hashing algorithm. It iterates through
        # each character in the key, multiplies the current hash value by 31 (a common prime number used in hashing),
        # and adds the ASCII value of the character. This process ensures that the same string will always produce
        # the same hash value.

        # return abs(hash(key)) % self.capacity  # This code causes error, on each turn hash value is different
        # Use a deterministic hashing algorithm for strings
        if type(key) is str:
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31) + ord(char)  # Simple hash function
            return abs(hash_value) % self.capacity
        else:
            return abs(hash(key)) % self.capacity

    def __len__(self):
        """No of elements in the dict"""
        return self.size

    def __str__(self):
        """Traverse through dict made using chaining."""
        # Traversing through all bucket in buckets, even if they are empty
        for ll_index in range(self.capacity):  # capacity = length of the buckets
            print(self.buckets[ll_index])  # printing each bucket/ll.

        return ""

    def __getitem__(self, key: Any) -> Any:
        """Get the corresponding value through key"""
        # bucket_index: the bucket no. in which this key-value node will go.
        bucket_index = self.hash_function(key)

        # Check if key already exists in that bucket.
        node_index = self.buckets[bucket_index].search_by_key(key)
        if node_index == -1:  # If the key doesn't exist
            raise ValueError("The key doesn't exist in the dict")
        else:  # If the key already exists
            # So get the value from node at node_index.
            return self.buckets[bucket_index].node_at_index(node_index).value

    def __delitem__(self, key: Any):
        """delete item by providing key."""
        bucket_index = self.hash_function(key)

        # Check if key already exists in that bucket.
        node_index = self.buckets[bucket_index].search_by_key(key)
        if node_index == -1:  # If the key doesn't exist
            raise ValueError("The key doesn't exist in the dict")
        else:  # Delete by key, if key exists
            self.buckets[bucket_index].delete_by_key(key)


D1 = Dictionary(3)
D1["python"] = 123  # 2
D1["java"] = 123  # 3
D1["C++"] = 123  # 2
D1["C"] = 123
D1["php"] = 123
D1["ruby"] = 0  # Rehashing happens here
# D1["java"] = 321
print(D1)

print(D1["ruby"])
del D1["java"]

print(D1)

