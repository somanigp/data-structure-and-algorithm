# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
# In simple words, a linked list consists of nodes where each node contains a data field and
# a reference(link) to the next node in the list.
# Our first node is where head points and we can access all the elements of the linked list using the head.

# A linked list is a type of linear data structure similar to arrays. It is a collection of nodes that are linked with
# each other. A node contains two things first is data and second is a link that connects it with another node.
# https://www.youtube.com/watch?v=-Yn5DU0_-lw&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=6

# Our first node is where head points and we can access all the elements of the linked list using the head.
# Last node points to null


# Create a Node class to create a node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Create a LinkedList class

# To iterate in a linked list, you need current node and position


class LinkedList:
	def __init__(self):
		self.head = None  # You access a LL through its head

	# Method to add a node at the beginning of LL
	def insert_at_beginning(self, data):
		new_node = Node(data)  # First always create a new Node out of data.
		if self.head is None:  # if a value is None use 'is None'
			self.head = new_node  # Head of the LL object will be the new_node, these functions will be on the
			# linked list object
			return
		else:
			new_node.next = self.head  # current head will become the new node's next
			self.head = new_node # and new_node will become the new head

	# Method to add a node at any index
	# Indexing starts from 0.

	def insert_at_index(self, data, index):
		new_node = Node(data)
		current_node = self.head
		position = 0
		if position == index:
			self.insert_at_beginning(data)
		else:
			while current_node is not None and position+1 != index:  # use 'is not' and 'is' None.
				# position+1 != index. meaning we have to change at pos which is just before index
				position += 1
				# If the index is out of bound then current node will become None below as last element
				# current_node.next is None
				current_node = current_node.next  # going to the next ele in a LL. iteration with help of next

			if current_node is not None:
				new_node.next = current_node.next
				current_node.next = new_node
			else:
				print("Index not present")

	# Method to add a node at the end of LL

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.head is None:  # LL doesnt have any Node
			self.head = new_node
			return

		current_node = self.head
		while current_node.next:  # while current_node.next exists. meaning while current_node.next is not None
			current_node = current_node.next

		current_node.next = new_node

	# Update node of a linked list
		# at given position
	def update_node(self, val, index):
		current_node = self.head
		position = 0
		if position == index:
			current_node.data = val
		else:
			while current_node is not None and position != index:
				position = position+1
				current_node = current_node.next

			if current_node is not None:
				current_node.data = val
			else:
				print("Index not present")

	# Method to remove the first node of a linked list
	def remove_first_node(self):
		if self.head is None:
			return

		self.head = self.head.next

	# Method to remove last node of linked list
	def remove_last_node(self):

		if self.head is None:
			return

		current_node = self.head
		while current_node.next.next:  # To reach second last node.
			# Thus current_node.next.next is null for second last node
			current_node = current_node.next

		current_node.next = None

	# Method to remove at given index
	def remove_at_index(self, index):
		if self.head is None:
			return

		current_node = self.head
		position = 0
		if position == index:
			self.remove_first_node()
		else:
			while current_node is not None and position+1 != index:
				position = position+1
				current_node = current_node.next

			if current_node is not None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")

	# Method to remove a node from a linked list
	def remove_node(self, data):
		current_node = self.head

		if current_node.data == data:
			self.remove_first_node()
			return

		while current_node is not None and current_node.next.data != data:
			current_node = current_node.next

		if current_node is None:
			return
		else:
			current_node.next = current_node.next.next  # removing the node

	# Print the size of linked list
	def size_of_ll(self):
		size = 0
		if self.head:
			current_node = self.head
			while current_node:
				size = size+1
				current_node = current_node.next
			return size
		else:
			return 0

	# print method for the linked list
	def print_ll(self):
		current_node = self.head
		while(current_node):
			print(current_node.data)
			current_node = current_node.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insert_at_end('a')
llist.insert_at_end('b')
llist.insert_at_beginning('c')
llist.insert_at_end('d')
llist.insert_at_index('g', 2)

# print the linked list
print("Node Data")
llist.print_ll()

# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)


# print the linked list again
print("\nLinked list after removing a node:")
llist.print_ll()

print("\nUpdate node Value")
llist.update_node('z', 0)
llist.print_ll()

print("\nSize of linked list :", end=" ")
print(llist.size_of_ll())



