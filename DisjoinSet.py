# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:01:44 2019

@author: suman
"""
from collections import defaultdict

class Node:
    
    def __init__(self, data):
        self.data = data
        self.rank = 0
        #self.parent = None
        self.parent = self
        
class DisjoinSet:
    
    def __init__(self, vertices):
        #self.set = {_: [] for _ in range(len(vertices))}
        self.set = defaultdict(list)
        
    def makeSet(self, data):
        node = Node(data)
        self.set[data] =  node
        
    def union(self, value1, value2):
        node1 = self.set[value1]
        node2 = self.set[value2]
        parent1 = self.findSet(node1)
        parent2 = self.findSet(node2)
        
        if parent1.data == parent2.data:
            return
        else:
            if parent1.rank == parent2.rank:
                parent1.rank = parent1.rank + 1
                parent2.parent = parent1
            elif parent1.rank > parent2.rank:     
                parent2.parent = parent1
            else:     
                parent1.parent = parent2
                
            
    def findSetFor(self, data):
        return self.findSet(self.set[data]).data

# =============================================================================
#     def findSet(self, node):
#         
#         while node.parent is not None:
#             node = node.parent
#             
#         return node    
# =============================================================================
        
# =============================================================================
#     def findSet(self, node):
#         
#         if node.parent is None:
#             return node
#         #path compression
#         node.parent = self.findSet(node.parent)
#         return node.parent
# =============================================================================
 
    def findSet(self, node):
        
        if node.parent is node:
            #return node.parent
            return node
        #path compression
        node.parent = self.findSet(node.parent)
        return node.parent
    
if __name__ == '__main__':
    
    disjoin_set = DisjoinSet(5)
    disjoin_set.makeSet(1)
    disjoin_set.makeSet(2)
    disjoin_set.makeSet(3)
    disjoin_set.makeSet(4)
    disjoin_set.makeSet(5)
    disjoin_set.makeSet(6)
    disjoin_set.makeSet(7)
    disjoin_set.makeSet(8)
    disjoin_set.makeSet(9)
    
    print("Parent for {} is {}".format(5, disjoin_set.findSetFor(5)))
    disjoin_set.union(1 ,2)
    disjoin_set.union(2 ,3)
    disjoin_set.union(4 ,5)
    disjoin_set.union(6 ,7)
    disjoin_set.union(5 ,6)
    disjoin_set.union(3 ,7)
    
    print("Parent for {} is {}".format(1, disjoin_set.findSetFor(1)))
    print("Parent for {} is {}".format(2, disjoin_set.findSetFor(2)))
    print("Parent for {} is {}".format(3, disjoin_set.findSetFor(3)))
    print("Parent for {} is {}".format(4, disjoin_set.findSetFor(4)))
    print("Parent for {} is {}".format(5, disjoin_set.findSetFor(5)))
    print("Parent for {} is {}".format(6, disjoin_set.findSetFor(6)))
    print("Parent for {} is {}".format(7, disjoin_set.findSetFor(7)))
        
        
        
        
