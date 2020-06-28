#implementation of stack using linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.link = None

class Stack:
	def __init__(self):
		self.head = None

	def push(self,data):
		n = Node(data)
		if self.head == None:
			self.head = n
		else:
			temp = self.head
			n.link = temp
			self.head = n
	def display_top_to_bottom(self):
		if self.head == None:
			raise Exception("No element found")
		else:
			temp = self.head
			while temp:
				print(temp.data, end = " ")
				temp = temp.link
			print()
	def pop(self):
		if self.head == None:
			raise Exception("No element for deletion")
		else:
			self.head = self.head.link

# s = Stack()
# l = [3,6,78,45,29]
# for i in l:
# 	s.push(i)
# t = s
# t.pop()
# t = Stack()
# t.push(67)
# t.display_top_to_bottom()
# print("*************")
# s.display_top_to_bottom()

###########################################################
if __name__ == "__main__":
	s = Stack()
	while True:
		print("********************************")
		print("press 1 for display")
		print("press 2 for push")
		print("press 3 for pop")
		print("press 9 for exit")
		print()
		n = int(input())
		if n==1:
			try:
				print("top-to-bottom")2
				s.display_top_to_bottom()
			except:
				print("Cannot show element from empty stack")
				continue
		if n==2:
			print("enter data to push:", end = " ")
			inp = int(input())
			s.push(inp)
		if n==3:
			try:
				s.pop()
			except:
				print("can\'t operate")
				continue
		if n==9:
			break



