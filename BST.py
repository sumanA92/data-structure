
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:39:31 2019

@author: venkata.annapureddy
"""

class Node:
    
    def __init__(self, data):
        self.data =  data
        self.left = None
        self.right = None
        
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=', ')
        if self.right is not None:
            self.right.inorder()
            
    def minValue(self, right):
        current = right
        while right.left is not None:
            current = right.left
            
        return current
    
    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
                
    def delete(self, data):
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

        next_min_node = self.minValue(self.right)   
        self.data = next_min_node.data
        self.right = self.right.delete(next_min_node.data)
        
        return self
                   
                
                
                           

root = Node(50)
#root = insert(root, 50) 
root.insert(30) 
root.insert(20) 
root.insert(40) 
root.insert(70) 
root.insert(60) 
root.insert(80) 

print("Inorder traversal of the given tree")
root.inorder() 

# =============================================================================
# print("\nDelete 20")
# root = deleteNode(root, 20) 
# print("Inorder traversal of the modified tree")
# inorder(root) 
# 
# print("\nDelete 30")
# root = deleteNode(root, 30) 
# print("Inorder traversal of the modified tree")
# inorder(root) 
# 
# =============================================================================
print("\nDelete 50")
root = root.delete(50) 
print("Inorder traversal of the modified tree")
root.inorder() 

# Python program to demonstrate delete operation 
# in binary search tree 

# A Binary Tree Node 
# =============================================================================
# class Node: 
# 
# 	# Constructor to create a new node 
# 	def __init__(self, key): 
# 		self.key = key 
# 		self.left = None
# 		self.right = None
# 
# 
# # A utility function to do inorder traversal of BST 
# def inorder(root): 
# 	if root is not None: 
# 		inorder(root.left) 
# 		print(root.key) 
# 		inorder(root.right) 
# 
# 
# # A utility function to insert a new node with given key in BST 
# def insert( node, key): 
# 
# 	# If the tree is empty, return a new node 
# 	if node is None: 
# 		return Node(key) 
# 
# 	# Otherwise recur down the tree 
# 	if key < node.key: 
# 		node.left = insert(node.left, key) 
# 	else: 
# 		node.right = insert(node.right, key) 
# 
# 	# return the (unchanged) node pointer 
# 	return node 
# 
# # Given a non-empty binary search tree, return the node 
# # with minum key value found in that tree. Note that the 
# # entire tree does not need to be searched 
# def minValueNode( node): 
# 	current = node 
# 
# 	# loop down to find the leftmost leaf 
# 	while(current.left is not None): 
# 		current = current.left 
# 
# 	return current 
# 
# # Given a binary search tree and a key, this function 
# # delete the key and returns the new root 
# def deleteNode(root, key): 
# 
# 	# Base Case 
# 	if root is None: 
# 		return root 
# 
# 	# If the key to be deleted is smaller than the root's 
# 	# key then it lies in left subtree 
# 	if key < root.key: 
# 		root.left = deleteNode(root.left, key) 
# 
# 	# If the kye to be delete is greater than the root's key 
# 	# then it lies in right subtree 
# 	elif(key > root.key): 
# 		root.right = deleteNode(root.right, key) 
# 
# 	# If key is same as root's key, then this is the node 
# 	# to be deleted 
# 	else: 
# 		
# 		# Node with only one child or no child 
# 		if root.left is None : 
# 			temp = root.right 
# 			root = None
# 			return temp 
# 			
# 		elif root.right is None : 
# 			temp = root.left 
# 			root = None
# 			return temp 
# 
# 		# Node with two children: Get the inorder successor 
# 		# (smallest in the right subtree) 
# 		temp = minValueNode(root.right) 
# 
# 		# Copy the inorder successor's content to this node 
# 		root.key = temp.key 
# 
# 		# Delete the inorder successor 
# 		root.right = deleteNode(root.right , temp.key) 
# 
# 
# 	return root 
# 
# =============================================================================
# Driver program to test above functions 
# =============================================================================
# """ Let us create following BST 
# 			50 
# 		/	 \ 
# 		30	 70 
# 		/ \ / \ 
# 	20 40 60 80 """
# 
# root = None
# root = insert(root, 50) 
# root = insert(root, 30) 
# root = insert(root, 20) 
# root = insert(root, 40) 
# root = insert(root, 70) 
# root = insert(root, 60) 
# root = insert(root, 80) 
# 
# print("Inorder traversal of the given tree")
# inorder(root) 
# 
# # =============================================================================
# # print("\nDelete 20")
# # root = deleteNode(root, 20) 
# # print("Inorder traversal of the modified tree")
# # inorder(root) 
# # 
# # print("\nDelete 30")
# # root = deleteNode(root, 30) 
# # print("Inorder traversal of the modified tree")
# # inorder(root) 
# # 
# # =============================================================================
# print("\nDelete 50")
# root = deleteNode(root, 50) 
# print("Inorder traversal of the modified tree")
# inorder(root) 
# =============================================================================

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
