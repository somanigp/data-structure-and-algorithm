# LL : Linear DS used to store data in non-continuous memory location. Collection of nodes. Nodes are not in continuous
# memory location 99%.

# Node Object: Has 2 attributes : data (Any, thus flexible) and address (Points to the next node)
# First pointer Head and Last pointer is Tail and addr. points to null.

# Array disadvantage : In array while performing write action (insert or delete) we need to start shifting elements and
# thus time complexity is O(n) for 1 write operation. So list size increases than time increases.
# Also in array a lot of memory is un-utilized, when doubling a large array.

# Thus for applications like to-do list, ll is better. So for ll write operations have order O(1), meaning constant
# Through ll, you don't need to waste memory.
# You can create stacks and queues with help of ll, which is better than with array.
# DLL and CLL can be created through ll.

# Array : Good for READ operations. As values are stored in continuous memory location.
# To get an ele-(pos of first element + index*size of each)

# LL : Bad for READ operations, as O(n), increases with len of ll. But good at right.

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None  # By default, Node object will have None value, ie not pointing to any other node.


# How to create individual nodes and connect them.
a = Node(1)  # node with data=1
b = Node(2)  # node with data=2
a.next = b  # 'a' node pointing to 'b' node.
b.next = Node(5)  # Can directly put Node object in .next instead of creating variable.
print(b.next.data)  # Getting data of next node.
print(id(a))  # Return the identity of an object. Objects memory address.

# Now :
print(a.next)  # <__main__.Node object at 0x000001FFD8DE3410>
print(int(0x000001FFD8DE3410))  # 2338700145296 . Hexadecimal to integer
print(b)  # <__main__.Node object at 0x000001FFD8DE3410>
print(id(b))  # basically a.next will point at object at memory location which belongs to b

