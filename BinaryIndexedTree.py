# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:04:37 2019

@author: suman
"""

def createTree(array):
    prefix_sum_array = [0] * (len(array)+1)
    for idx, value in enumerate(array):
        updateBinaryIndexedTree(prefix_sum_array, value, idx, False)
    
    return prefix_sum_array    
        
def updateBinaryIndexedTree(prefix_sum_array, value, idx, isUpdate=True):
    if isUpdate:
        next_idx = getNextIdx(idx)
    else:
        next_idx = idx + 1
        
    if next_idx < len(prefix_sum_array):
        prefix_sum_array[next_idx] += value
        updateBinaryIndexedTree(prefix_sum_array, value, next_idx)

# =============================================================================
# def updateBinaryIndexedTree(prefix_sum_array, value, idx):
#     
#     next_idx = idx + 1
#     while next_idx < len(prefix_sum_array):
#         prefix_sum_array[next_idx] += value
#         next_idx = getNextIdx(next_idx)
# =============================================================================

def fetchSum(prefix_sum_array, idx, isUpdate=False):
    sum = 0
    if isUpdate:
        next_idx = getParentIdx(idx)
    else:
        next_idx = idx + 1
        
    if next_idx > 0:
        sum += prefix_sum_array[next_idx]
        subArraySum(prefix_sum_array, next_idx, True)
        
    return sum    

# =============================================================================
# def subArraySum(prefix_sum_array, idx):
#     sum = 0
#     next_idx = idx + 1
#         
#     while next_idx > 0:
#         sum += prefix_sum_array[next_idx]
#         next_idx = getParentIdx(next_idx)
#         
#     return sum    
# =============================================================================

def subArraySum(prefix_sum_array, start_idx, end_idx):
     
     start_idx_sum = 0
     next_idx = start_idx + 1
     while next_idx > 0:
         start_idx_sum += prefix_sum_array[next_idx]
         next_idx = getParentIdx(next_idx)
     
     end_idx_sum = 0
     next_idx = end_idx + 1
     while next_idx > 0:
         end_idx_sum += prefix_sum_array[next_idx]
         next_idx = getParentIdx(next_idx)
         
     return end_idx_sum - start_idx_sum  
        
def getNextIdx(idx):
    return idx + (idx & -idx)

def getParentIdx(idx):
    return idx - (idx & -idx)

array = [1, 2, 3, 4, 5, 6, 7]
binary_indexed_tree = createTree(array)
print('Sum upto index {} is {}'.format(4, fetchSum(binary_indexed_tree, 3)))
print('Sum upto index {} is {}'.format('4-6', subArraySum(binary_indexed_tree, 3 , 5)))