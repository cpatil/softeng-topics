class Node:

	def __init__(self, data=None, next=None):
		## data of the node
		self.data = data
		## next pointer
		self.next = next
	
	def get_data(self):
		return self.data

	def get_next(self):
		return self.next
	
	def set_next(self, new_next):
		self.next = new_next

class LinkedList:

	def __init__(self):
		## initializing the head with None
		self.head = None

	def insert(self, data):
		## check whether the head is empty or not
		new_node = Node(data)

		if self.head:
			## getting the last node
			last_node = self.head
			while last_node.next != None:
				last_node = last_node.next

			## assigning the new node to the next pointer of last node
			last_node.next = new_node

		else:
			## head is empty
			## assigning the node to head
			self.head = new_node
	
	def size(self):
		current = self.head
		cnt = 0

		while current:
			cnt += 1
			current = current.get_next()
		
		print(cnt)

	def search(self, data):
		current = self.head
		found = False

		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		
		if current is None:
			raise ValueError("Data not in list")
		
		print(current)

	def delete(self, data):
		current = self.head
		previous = None
		found = False

		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		
		if current is None:
			raise ValueError("Data not in list")

		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def display(self):
		## variable for iteration
		temp_node = self.head

		## iterating until we reach the end of the linked list
		while temp_node != None:
			## printing the node data
			print(temp_node.data, end='->')

			## moving to the next node
			temp_node = temp_node.next

		print('Null')


if __name__ == '__main__':
	## instantiating the linked list
	linked_list = LinkedList()

	## inserting the data into the linked list
	linked_list.insert(1)
	linked_list.insert(2)
	linked_list.insert(3)
	linked_list.insert(4)
	linked_list.insert(5)
	linked_list.insert(6)
	linked_list.insert(7)

	## printing the linked list
	linked_list.display()

	linked_list.size()

	linked_list.search(6)

	linked_list.delete(6)

	linked_list.display()