# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:33:51 2019

@author: suman
"""

from  numpy.random import randint

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if data <= self.data:
            if self.left == None :
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
                
    def contains(self, data):
        if self.data == data:
            return True
        elif data < self.data:
            if self.left == None:
               return False 
            else:
                return self.left.contains(data)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(data)
             
    def printOrder(self):
        if self.left != None:
            self.left.printOrder()
        
        print(self.data, end=', ')
        
        if self.right != None:
            self.right.printOrder()
            
if __name__ == '__main__':
    node = Node(5)
    for i in range(5):
        data = randint(0, 10)
        node.insert(data)       
    
    node.printOrder()
    print(node.contains(5))
    print(node.contains(6)) 
    print(node.contains(7))                     
        

    