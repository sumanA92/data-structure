# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Node:
    
    def __init__(self, data):
        self.data =  data;
        self.next = None;
        
class LinkedList:
    
    def __init__(self):
        self.head = None;
        
    def append(self, data):
        
        if self.head is None:
            self.head = Node(data);
            return;
            
        current = self.head;
        while current.next is not None:
            current = current.next;
    
        current.next = Node(data);
            
    def prepend(self, data):
        
        newHead = Node(data);
        newHead.next = self.head;
        self.head = newHead;
        
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
             
        
            
        