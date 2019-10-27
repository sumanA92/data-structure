# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:47:51 2019

@author: suman
"""
import sys
from numpy.random import randint
 
class SegmentTree:
    
    def __init__(self, array):
        self.array = array
        self.segment_tree = [0] * (2 * len(array) -1 )
        

    def constructMinTree(self, low, high, pos):
        if low == high: 
            self.segment_tree[pos] = self.array[low]
            return
        
        mid = (low + high) // 2
        self.constructMinTree(low, mid, 2 * pos + 1)
        self.constructMinTree(mid+1, high, 2 * pos + 2)
        self.segment_tree[pos] = min(self.segment_tree[2 * pos + 1], self.segment_tree[2 * pos + 2])
        
        
    def queryMin(self, qlow, qhigh, low, high, pos):
        
        if qlow <= low and qhigh  >= high:
            return self.segment_tree[pos]
        elif qlow > high or qhigh < low:
            return sys.float_info.max
        
        mid = (low + high) // 2
        return min(self.queryMin(qlow, qhigh, low, mid, 2 * pos + 1),
                   self.queryMin(qlow, qhigh, mid+1, high, 2 * pos + 2))
            
    def constructMaxTree(self, low, high, pos):
        
        if low == high:
            self.segment_tree[pos] = self.array[low]
            return
        
        mid = (low + high) // 2
        self.constructMaxTree(low, mid, 2 * pos + 1)
        self.constructMaxTree(mid+1, high, 2 * pos + 2)
        self.segment_tree[pos] = max(self.segment_tree[2 * pos + 1], self.segment_tree[2 * pos + 2])
        
        
    def queryMax(self, qlow, qhigh, low, high, pos):
        
        if qlow <= low and qhigh  >= high:
            return self.segment_tree[pos]
        elif qlow > high or qhigh < low:
            return sys.float_info.max
        
        mid = (low + high) // 2
        return max(self.queryMin(qlow, qhigh, low, mid, 2 * pos + 1),
                   self.queryMin(qlow, qhigh, mid+1, high, 2 * pos + 2))            
            

if __name__ == '__main__':
    
    arry = []
    for i in range(7):
        arry.append(randint(0, 30))
        
    print("Array : {}".format(arry))    
    seg_tree = SegmentTree(arry)
    seg_tree.constructMinTree(0, len(arry)-1, 0)
    print("min segement tree : ",seg_tree.segment_tree)
    print(seg_tree.queryMin(0, l
                            en(arry)-1, 0, len(arry)-1, 0))
    print(seg_tree.queryMin(3, len(arry)-1, 0, len(arry)-1, 0))
    print(seg_tree.queryMin(1, 4, 0, len(arry)-1, 0))