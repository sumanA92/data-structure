# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:09:01 2019

@author: suman
"""

#A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class stack:
    
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            raise Exception("Queue is empty")
        return self.top.data        
    
    def push(self, data):
         new_node = Node(data)
         if self.top is not None:
             new_node.next = self.top
             
         self.top = new_node
       
    def pop(self):
        if self.top is None:
            raise Exception('Queue is empty')
        temp = self.top
        self.top = self.top.next
        
        return temp.data
      
    def printStack(self):
        temp = self.top
        if temp is None:
            print('Stack is empty')
            return
        while temp is not None:
            print(temp.data, end=', ')
            temp = temp.next
        
        print()
            
if __name__ == '__main__':
    stack = stack()
    
    print(stack.isEmpty())
    stack.printStack()
    stack.push(3)
    stack.push(4)    
    stack.push(4)    
    stack.push(4)  
    
    print(stack.peek())
    print(stack.pop())
    stack.printStack()
    
    stack.push(5)
    stack.printStack()
    stack.printStack()
    print(stack.pop())
    stack.printStack()
