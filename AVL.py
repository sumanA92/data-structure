# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:26:14 2019

@author: venkata.annapureddy
"""
#https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
class Node:
    
    def __init__(self, data):
        self.data =  data
        self.height = 1
        self.left = None
        self.right = None
        
    def minValue(self, right):
        current = right
        while current.left is not None:
            current = right.left
            
        return current
    
    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left = self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right = self.right.insert(data)
                
        balance = getBalance(self)
        if balance > 1:
            if getBalance(self.left) > 0:
                return self.rotateRight()
            elif getBalance(self.right) < 0:
                self.left = self.left.rotateLeft()
                return self.rotateRight()
            
        if balance < -1:
            if getBalance(self.right) < 0:
                return self.rotateLeft()
            elif getBalance(self.left) > 0:
                self.right = self.right.rotateLeft()
                return self.rotateLeft() 
        print("hello there",getHeight(self.left),getHeight(self.right),self.data);
        self.height = max(getHeight(self.left), getHeight(self.right)) + 1  
        print("after increasing the heignt",self.height,self.data)
        return self
        
    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            next_min_node = self.minValue(self.right)   
            self.data = next_min_node.data
            self.right = self.right.delete(next_min_node.data)
        
        balance = getBalance(self)
        if balance > 1:
            if getBalance(self.left) > 0:
                return self.rotateRight()
            elif getBalance(self.right) < 0:
                self.left = self.left.rotateLeft()
                return self.rotateRight()
            
        if balance < -1:
            if getBalance(self.right) < 0:
                return self.rotateLeft()
            elif getBalance(self.left) > 0:
                self.right = self.right.rotateLeft()
                return self.rotateLeft()    
        
        self.height = max(getHeight(self.left), getHeight(self.right)) + 1
        return self
    
    def rotateRight(self):
        root = self
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        
        root.height = max(getHeight(root.left), getHeight(root.right)) + 1
        new_root.height = max(getHeight(new_root.left), getHeight(new_root.right)) + 1
        
        return new_root
    
    
    def rotateLeft(self):
        root = self
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        
        root.height = max(getHeight(root.left), getHeight(root.right)) + 1
        new_root.height = max(getHeight(new_root.left), getHeight(new_root.right)) + 1
        
        return new_root
    
    
def getHeight(root):
    return 0 if root is None else root.height

def getBalance(root):
    return getHeight(root.left) - getHeight(root.right)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=', ')
        inOrder (root.right)
    
myTree = Node(9) 
nums = [5, 10, 0, 6, 11, -1, 1, 2] 
  
for num in nums:
   print("start of for loop",num) 
   myTree = myTree.insert(num)
   print("seperating methods",num)
  
# Preorder Traversal 
print("Inorder Traversal after insertion -") 
inOrder(myTree) 
print() 
  
# Delete 
key = 10
myTree = myTree.delete(key) 
  
# Preorder Traversal 
print("Inorder Traversal after deletion -") 
inOrder(myTree) 
print() 
      