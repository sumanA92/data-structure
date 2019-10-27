# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:31:33 2019

@author: suman
"""
#heap data structure in python(heapq)in https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
#https://www.geeksforgeeks.org/merge-two-sorted-arrays-python-using-heapq/
#https://www.geeksforgeeks.org/max-heap-in-java/
#https://www.geeksforgeeks.org/binary-heap/
from numpy.random import randint
class MinHeap:
    
    def __init__(self):
        self.capcity = 10;
        self.size = 0
        self.arr = [0] * self.capcity
        
        
    def leftChildIndex(self, idx):
        return 2 * idx + 1
    
    def rightChildIndex(self, idx):
        return 2 * idx + 2
    
    def parentIndex(self, leftChildIdx):
        return (leftChildIdx - 1) // 2
    
    def hasLeftChild(self, idx):
        return self.rightChildIndex(idx) < self.size
    
    def hasRightChild(self, idx):
        return self.rightChildIndex(idx) < self.size
    
    def hasParent(self, leftChildIdx):
        return self.parentIndex(leftChildIdx) >= 0
    
    def swap(self, idx1, idx2):
        self.arr[idx1], self.arr[idx2] = self.arr[idx2], self.arr[idx1]
        
    def ensureExtraCapacity(self):
        if self.size == self.capcity :
            #arr = [0] * (2 * self.capcity)
            #arr[:self.size] =self.arr
            self.arr.extend([0] * self.capcity)
            self.capcity *= 2
        
    def peek(self):
        if self.size == 0 :
            raise Exception('heap  is empty')
        return self.arr[0]    
        
    def poll(self):
        if self.size == 0 :
            raise Exception('Heap is empty')
            
        min = self.arr[0]
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], 0
        self.size -= 1
        self.heapifyDown(0)
        return min
        
    def push(self, value):
        self.ensureExtraCapacity()
        self.arr[self.size] = value
        self.size += 1
        self.heapifyUp(self.size - 1)
        
    def heapifyDown(self, idx):
        smallIdx = idx
        if self.hasLeftChild(idx) and self.arr[self.leftChildIndex(idx)] < self.arr[smallIdx] :
            smallIdx = self.leftChildIndex(idx)
        if self.hasRightChild(idx) and self.arr[self.rightChildIndex(idx)] < self.arr[smallIdx] :
            smallIdx = self.rightChildIndex(idx)
        if smallIdx != idx:    
            self.swap(idx, smallIdx)
            self.heapifyDown(smallIdx)
    
# =============================================================================
#     def heapifyDown(self, idx):
#         while self.hasLeftChild(idx):
#             smallIdx = self.leftChildIndex()    
#             if self.hasRightChild(idx) and self.arr[self.rightChildIndex(idx)] < self.arr[smallIdx] :
#                 smallIdx = self.rightChildIndex(idx)
#             if self.arr[idx] < self.arr[smallIdx]:
#                 break
#             else:
#                 self.swap(idx, smallIdx)
#                 idx = smallIdx    
# =============================================================================
    def heapifyUp(self, idx):
        if self.hasParent(idx) and self.arr[self.parentIndex(idx)] > self.arr[idx] :
            self.swap(idx, self.parentIndex(idx))
            self.heapifyUp(self.parentIndex(idx))      

# =============================================================================
#     def heapifyUp(self, idx):
#         while self.hasParent(idx) and self.arr[self.parentIndex(idx)] > self.arr[idx] :
#             self.swap(idx, self.parentIndex(idx))
#             idx = self.parentIndex(idx)
# =============================================================================


if __name__ == '__main__' :
    min_heap = MinHeap()
    for i in range(8):
        element = randint(0, 20)
        min_heap.push(element)
    print(list(min_heap.arr))
    print(min_heap.poll())
    print(list(min_heap.arr))
    print(min_heap.peek())    