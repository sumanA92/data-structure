# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:42:54 2019

@author: suman
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            raise Exception("Stack is empty")
        return self.head.data        
    
    def add(self, data):
         new_node = Node(data)
         if self.tail is not None:
             self.tail.next = new_node
             
         self.tail = new_node
         if self.head is None:
             self.head = new_node
   
    def remove(self):
        if self.head is None:
            raise Exception('Stack is empty')
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        
        return temp.data
    
    def printQueue(self):
            temp = self.head
            if temp is None:
                print('Queue is empty')
                return
            while temp is not None:
                print(temp.data, end=', ')
                temp = temp.next
            
            print()
            
if __name__ == '__main__':
    queue = queue()
    
    print(queue.isEmpty())
    queue.printQueue()
    queue.add(3)
    queue.add(4)    
    queue.add(4)    
    queue.add(4)  
    
    print(queue.peek())
    print(queue.remove())
    queue.printQueue()
    
    queue.add(5)
    queue.printQueue()
    queue.printQueue()
    print(queue.remove())
    queue.printQueue()
    