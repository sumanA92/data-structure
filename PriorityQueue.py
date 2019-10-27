# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:44:06 2019

@author: suman
"""
from numpy.random import randint

class PrioritQueue(object):
    
    def __init__(self):
        self.nodes = [None]
        self.insert_count = 0
        
    def _is_higher_than(self, a, b):
        return b[1] < a[1] or (a[1] == b[1] and a[2] < b[2])
    
    def peek(self):
        if len(self.nodes) == 1:
            return None
        else:
            self.nodes[1][0]
            
    def add(self, value, priority):
        new_node_index = len(self.nodes)
        self.insert_count += 1
        self.nodes.append([value, priority, self.insert_count])
        self._heapify(new_node_index)

    def pop(self):
        if len(self.nodes) == 1:
            raise LookupError('Heap is empty')
        
        result = self.nodes[1][0]
        
        empty_space_index = 1
        while empty_space_index * 2 < len(self.nodes):
            
            left_child_index = empty_space_index * 2
            right_child_index = empty_space_index * 2 + 1
            
            if(len(self.nodes) < right_child_index or 
                self._is_higher_than(self.nodes[left_child_index], self.nodes[right_child_index]) ):
                self.nodes[empty_space_index] = self.nodes[left_child_index]
                empty_space_index = left_child_index
            else:
                self.nodes[empty_space_index] = self.nodes[right_child_index]
                empty_space_index = right_child_index
                
                
            last_node_index = len(self.nodes) - 1
            self.nodes[empty_space_index] = self.nodes[last_node_index]
            self._heapify(empty_space_index)
            
            self.nodes.pop()
            
            return result
        
    def _heapify(self, new_node_index):
        while 1 < new_node_index:
            new_node = self.nodes[new_node_index]
            parent_index = new_node_index // 2
            parent_node = self.nodes[parent_index]
            
            if self._is_higher_than(self.nodes[parent_index], self.nodes[new_node_index]):
                break
            
            self.nodes[new_node_index], self.nodes[parent_index] = parent_node, new_node
            
            new_node_index = parent_index
   
# =============================================================================
#     def pop(self):
#         result = self.nodes[1][0]
#         self.nodes[1] = self.nodes.pop()
#         self._heapifyDown(1)
#         return result
#                 
#     def _heapifyDown(self, parent_node_index):
#             while parent_node_index * 2 < len(self.nodes):
#                 left_child_index = parent_node_index * 2
#                 right_child_index = parent_node_index * 2 + 1
#                 swap_index = parent_node_index
#                 
#                 if(len(self.nodes) < right_child_index or 
#                   self._is_higher_than(self.nodes[left_child_index], self.nodes[right_child_index]) ):
#                     swap_index = left_child_index
#                 else:
#                     swap_index = right_child_index
#                 
#                 if self._is_higher_than(self.nodes[parent_node_index], self.nodes[swap_index]):
#                     break
#                 self.nodes[parent_node_index], self.nodes[swap_index] = self.nodes[swap_index], self.nodes[parent_node_index]
#                 parent_node_index = swap_index
# =============================================================================

if __name__ == '__main__':
    priority_queue = PrioritQueue()
    for i in range(5):
        value = randint(1, 10)
        priority = randint(1, 10)
        priority_queue.add(value, priority)
    
    
    for node in priority_queue.nodes:
        print(node)