from typing import Any


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Linked List Class. Note a ll is accessed through its head. Thus, only has a head.
class LinkedList:
    # 4 Main Operations:
    # Insert: through Head, Tail (append) , In middle.
    # Traverse: print
    # Delete: Head, Tail, value (remove method), index based.
    # Search: using value or index.

    def __init__(self):
        # head is the first node in a ll. When head = None, means empty ll.
        # self.head is a Node.
        self.head = None  # Means empty liked list. That is the initial object should be empty.
        self.n = 0  # No. of nodes in a ll.

    def __len__(self):  # length of the ll = no. of nodes in ll
        return self.n

    def __str__(self) -> str:
        # Work with pointers for ll.
        pointer = self.head  # Starting with first node
        result: str = ''
        # If ll is empty
        if pointer is None:
            return result
        while pointer.next is not None:  # Checking if the pointer is the Tail.
            result += str(pointer.data) + ' -> '  # Convert all data to str.
            pointer = pointer.next  # Making pointer the next node. Going to the next node
        result += str(pointer.data)  # Pointer now is the Tail here.
        return result

    def insert_head(self, value: Any):  # Taking data as input and not Node,
        # as for user Node is only inner working of ll and doesn't bother them.
        # Create a node for that value
        new_node = Node(value)
        new_node.next = self.head  # new node will point to node which is at head
        self.head = new_node  # Now after that connection, head will point to new node
        self.n += 1

    def insert_tail(self, value: Any):  # append
        new_node = Node(value)  # As Node is created here, new_node.next is None
        # If empty ll, then head=None, thus pointer.next will give error.
        if self.head is None:
            self.head = new_node
        else:
            # Setting pointer to first Node
            pointer = self.head
            # when pointer.next is None, which means when pointer=Tail. Then wont go in while.
            while pointer.next:  # This is 'while pointer.next is not None'.
                pointer = pointer.next  # Moving pointer to the next node.
            pointer.next = new_node  # Pointer is TAIL here.
        self.n += 1  # Increasing no. of nodes here.

    def insert_after(self, after: Any, value: Any):
        # New node
        new_node = Node(value)
        # Traverse to the point where pointer.data = value.
        pointer = self.head
        if pointer is None:
            raise ValueError("Empty LinkedList")
        while pointer.data != after:
            # Case: No pointer.data matches after.
            if pointer.next is None:  # Here pointer will be TAIL, and above we are
                # checking if the data of last node is = to after. If not then break with pointer = TAIL
                raise ValueError("'After' Item Not Found")
            pointer = pointer.next
        new_node.next = pointer.next  # Note location of pointer.next node is only with pointer,
        # thus pointer is pointed to new node in 2nd step.
        pointer.next = new_node
        self.n += 1

    def clear(self):
        """Make LL empty"""
        # Thus condition of empty ll to be applied here
        self.head = None
        self.n = 0

    def delete_from_head(self):  # pop left.
        """Delete the first element from start"""
        if self.head is None:
            raise ValueError("The list is empty")
        self.head = self.head.next  # pointing head to Node/None after head.
        self.n -= 1  # Decreasing the length.

    def delete_from_tail(self):  # pop
        """Delete the last element from ll"""
        pointer = self.head
        if pointer is None:
            raise ValueError("The list is empty")
        elif pointer.next is None:
            self.head = None
            self.n = 0
            # return self.delete_from_head()  # returns the call for delete_from_head function.
        else:
            while pointer.next.next is not None:
                pointer = pointer.next
            pointer.next = None
            self.n -= 1

    def delete_by_value(self, value: Any):
        """Deletes the Node/Item which has data=value"""
        pointer = self.head

        # Empty LL
        if pointer is None:
            raise ValueError("LL is empty")

        # Only one item in the LL
        if pointer.next is None:
            if pointer.data == value:
                return self.delete_from_head()
            else:
                raise ValueError("Value not found")

        # When LL size is >= 2.
        if pointer.data == value:  # Checking if first element matches
            return self.delete_from_head()
        # Need to stop at Node before the node containing the data=value
        while pointer.next.data != value:
            # If no data found which is = to value and there is nothing to delete
            if pointer.next.next is None:
                raise ValueError("Value not found")
            pointer = pointer.next
        pointer.next = pointer.next.next
        self.n -= 1

    def search_by_value(self, value: Any) -> int:  # Index
        """Returns the index of the value provided"""
        pointer = self.head
        index = 0

        # Empty LL
        if pointer is None:
            raise ValueError("LL is empty")

        # If pointer node data=value then returns the index of the pointer
        while pointer.data != value:
            if pointer.next is None:
                raise ValueError("Value not found")
            pointer = pointer.next
            # Index of current pointer updated.
            index += 1
        return index

    def __getitem__(self, index: int) -> Any:
        """Returns the value at index passed."""
        # Check if index out of bounds
        if not 0 <= index < self.n:
            raise IndexError("Index out of bounds")

        if self.head is None:
            raise ValueError("LL is empty")

        pointer = self.head
        # Loops index no of times
        for i in range(index):  # 0 + iterations = iterations ( thus lands on correct index )
            pointer = pointer.next
        # Pointer is the node at index 'index'.
        return pointer.data


# NOTE: When you import this file all its code will run unless you mention __name__ == "__main__".
# If no __name__ == "__main__", then all these ll print statement will execute
if __name__ == "__main__":
    ll = LinkedList()  # head is None
    ll.insert_head(1)  # head will be 1->None
    ll.insert_head(2)
    ll.insert_head(3)  # 3->2->1->None
    ll.insert_tail(0)
    ll.insert_tail(2)
    print(ll, len(ll))
    ll.insert_after(2, 10)
    print(ll, len(ll))
    # ll.clear()
    # print('ll is ' + str(ll))
    # ll.insert_after(200, 10) # raise ValueError("'After' Item Not Found")
    ll.delete_from_head()
    ll.delete_from_tail()
    print(ll, len(ll))
    ll.delete_by_value(10)
    ll.insert_tail(11)
    ll.insert_tail(12)
    ll.insert_tail(13)
    ll.insert_tail(14)
    print(ll)
    ll.delete_by_value(11)
    ll.delete_by_value(12)
    print(ll, len(ll))
    print(ll.search_by_value(13))
    print(ll[2])
# NOTE:
# for i in range(0):  # Doesn't get executed.
