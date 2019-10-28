# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 01:35:16 2019
@author: suman
"""

from numpy.random import randint

# =============================================================================
# def mergeSort(array, left, right):
#     if left >= right:
#         return
#         
#     temp = [0] * len(array)
#     mid = (left + right) // 2
#     mergeSort(array, left, mid)
#     mergeSort(array, mid+1, right)
#     mergeHalves(array, temp, left, right)
# 
# def mergeHalves(array, temp, leftSrart, rightEnd):
#     
#      leftEnd = (leftSrart + rightEnd) // 2
#      rightStart = leftEnd + 1
#      
#      left = leftSrart
#      right = rightStart
#      index = leftSrart
#      
#      while left <= leftEnd or right <=rightEnd:
#          if left <= leftEnd and right <=rightEnd:
#              if array[left] > array[right]:
#                  temp[index] = array[right]
#                  right += 1
#              else:
#                  temp[index] = array[left]
#                  left += 1
#          elif left <= leftEnd:
#              temp[index] = array[left]
#              left += 1
#          else:
#              temp[index] = array[right]
#              right += 1
#          index += 1    
#      
#      array[leftSrart:rightEnd+1] = temp[leftSrart:rightEnd+1]
#      
# =============================================================================

def mergeSort(array, left, right):
    if left >= right:
        return
        
    mid = (left + right) // 2
    mergeSort(array, left, mid)
    mergeSort(array, mid+1, right)
    mergeHalves(array, left, right)

def mergeHalves(array , leftSrart, rightEnd):
    
     leftEnd = (leftSrart + rightEnd) // 2
     rightStart = leftEnd + 1
     
     left = leftSrart
     right = rightStart
     temp = []
     while left <= leftEnd and right <=rightEnd:
         if array[left] > array[right]:
             temp.append(array[right])
             right += 1
         else:
             temp.append(array[left])
             left += 1
     
     if left <= leftEnd or right <=rightEnd:         
         temp.extend(array[left:leftEnd+1] if left <= leftEnd else array[right:rightEnd+1])
     array[leftSrart:rightEnd+1] = temp     
     
     
array = randint(0, 50, 10)
print("Unsorted list : {}".format(array))
mergeSort(array, 0, len(array)-1)
print("Sorted list : ", array)


def quickSort(array, left, right):
    if left >= right:
        return
    try:
        index = partition(array, left, right)
        print(index, array)
        quickSort(array, left, index-1)
        quickSort(array, index, right)
    except Exception as error:
        print(error)


def partition(array, left, right):
     
     mid = (left+right) // 2
     mid_value = array[mid]
     while left <= right:
         if array[left] >= mid_value and array[right] <= mid_value:
             array[left], array[right] = array[right], array[left]
             left += 1
             right -= 1
         elif array[left] < mid_value:
             left += 1
         elif array[right] > mid_value:
             right -= 1
     return left


def partition2(array, left, right):
    
    mid = (left+right) // 2
    mid_value = array[mid]
    print(mid, mid_value , left, right)
    try:
        while left <= right:
            #print(left ,right)
            while array[left] < mid_value:
                left += 1
            
            while array[right] > mid_value:
                right -= 1
                
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
            print(left , right,"fasf")
    except Exception as error:
        #print(error)
        pass
    return left

array = randint(0, 50, 10)
#array = [30, 25, 22, 29, 22, 44, 14,  0, 20, 35]
print("Unsorted list : {}".format(array))
quickSort(array, 0, len(array)-1)
print("Sorted list : ", array)
