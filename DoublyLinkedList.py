# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Advantages over singly linked list
#1) A DLL can be traversed in both forward and backward direction.
#2) The delete operation in DLL is more efficient if pointer to the node to be deleted is given.
#3) We can quickly insert a new node before a given node.
#In singly linked list, to delete a node, pointer to the previous node is needed. To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node using previous pointer.


#Disadvantages over singly linked list
#1) Every node of DLL Require extra space for an previous pointer. It is possible to implement DLL with single pointer though (See this and this).
#2) All operations require an extra pointer previous to be maintained. For example, in insertion, we need to modify previous pointers together with next pointers. For example in following functions for insertions at different positions, we need 1 or 2 extra steps to set previous pointer.

#Insertion
#A node can be added in four ways
#1) At the front of the DLL
#2) After a given node.
#3) At the end of the DLL
#4) Before a given node.

#Deletion become a lot easier.
#Extra memory for previous pointer
#Linked list of integer
#Single linked list - data - 4 + 8 for pointer
#Single linked list - data - 4 + 8 for next pointer + 8 for previous pointer

class Node:
    
    def __init__(self, data):
        self.data =  data;
        self.next = None;
        self.prev = None;
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None;
        self.last = None
        
        
    def push(self, data):
        
        newNode = Node(data);
        newNode.next = self.head;
        newNode.prev = None;
        
        if self.head is not None:
           self.head.prev = newNode
           
        self.head = newNode   
        
    def insertAfter(self, prev_node, data):
        
        if prev_node is None:
            print("Previous Should not be null")
            return;
            
        new_node = Node(data)
        new_node.prev = prev_node
        
        if prev_node.next is not None:
            new_node.next = prev_node.next
            prev_node.next.prev = new_node
            
        prev_node.next = new_node
    
    def insertBefore(self, next_node, data):
        
        if next_node is None:
            print("This does not exists in DLL")
            return;
            
        new_node = Node(data)
        new_node.next = next_node
        
        if next_node.prev is not None:
            new_node.prev = next_node.prev
            next_node.prev.next = new_node
            
        next_node.prev = new_node
    
    def append(self, data):
        
        new_node = Node(data)
        new_node.next = None
        
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return;
            
        while self.last.next is not None:
            self.last = self.last.next;
    
        newNode = Node(data);
        current.next = newNode
        newNode.prev = current
        
    def deletewithValue(self, data):
        
        if self.nead is None:
            return;
            
        if self.head.data == data:
            self.head = self.head.next;
            return;
        
        current = self. head;
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next;
                return;
            current = current.next;

    def printList(self):
        
        current = self.head;
        while current.next is not None:
            print(current.data, end=', ');                
            current = current.next;

 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList()
    llist.append(1)
    llist.append(5)
    llist.append(6)
    llist.append(7)
    llist.append(8)
    llist.append(2)
    llist.append(3)
    
    print(llist)
    llist.printList()
             
        
            
        