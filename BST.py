#Binary Search Tree
#@punzo.am
#initialize Base
import sys

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
	
	#insert node into to tree based on value
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
			else:
				self.data = data

	#function for looking up a specific value in the tree
	def lookup(self, data, parent=None):
		if data < self.data:
			if self.left is None:
				return None, None
			return self.left.lookup(data, self)
		elif data > self.data:
			if self.right is None:
				return None, None
			return self.right.lookup(data, self)
		else:
			return self, parent
	#function to delete a value from the tree
	def delete(self, data):
		node, parent = self.lookup(data)
		if node is not None:
			children_count = node.children_count()
		if children_count == 0:
			if parent:
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
				del node
			else:
				self.data = None
		elif children_count == 1:
			if node.left:
				n = node.left
			else:
				n = node.right
			if parent:
				if parent.left is node:
					parent.left = n
				else:
					parent.right = n
				del node
			else:
				self.left = n.left
				self.right = n.right
				self.data = n.data
		else:
			parent = node
			successor = node.right
			while successor.left:
				parent = successor
				successor = successor.left
			node.data = successor.data
			if parent.left == successor:
				parent.left = successor.right
			else:
				parent.right = successor.right

	def children_count(self):
		cnt = 0
		if self.left:
			cnt +=1
		if self.right:
			cnt +=1
		return cnt

	def print_tree(self):
		if self.left:
			self.left.print_tree() 
			
		print (self.data)
		if self.right:
			self.right.print_tree()


		
root = Node(10)
my_tree = [5, 15, 10, 9, 7, 2, 1, 4, 3, 8, 27, 40]
for i in my_tree:
	root.insert(i)
root.print_tree()
root.delete(5)
root.print_tree()







