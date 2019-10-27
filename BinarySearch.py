# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:10:18 2019

@author: suman
"""
from numpy.random import randint

def bubbleSort(array):
    
    isSorted = False
    lastUnsorted = len(array)-1
    
    while not isSorted:
        isSorted = True
        for idx in range(lastUnsorted):
            if array[idx] > array[idx+1]:
                array[idx], array[idx+1] = array[idx+1], array[idx]
                isSorted = False
        lastUnsorted -= 1
        

def isContainsKey(sortedArry, key):
    #return binaySearchRecursive(sortedArry, key, 0, len(sortedArry)-1)
    return binaySearchIterative(sortedArry, key)
    

def binaySearchRecursive(sortedArray, key, low, high):
    #print("low : {} | high : {}".format(low, high))
    
    try:
        if low >= high:
            return False
         
        mid = (low + high) // 2
        
        if sortedArray[mid] == key:
            return True
        elif sortedArray[mid] > key:
            return binaySearchRecursive(sortedArray, key, low, mid-1)
        else:     
            return binaySearchRecursive(sortedArray, key, mid+1, high)
    except Exception as ex:
        print(ex)

def binaySearchIterative(sortedArray, key):
    #print("low : {} | high : {}".format(low, high))
        left = 0
        right = len(sortedArray) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if sortedArray[mid] == key:
                return True
            elif sortedArray[mid] > key:
                right = mid - 1
            else:     
                left = mid + 1
                
        return False
    
array = randint(0, 50, 10)
print("Unsorted list : {}".format(array))
bubbleSort(array)
print("Sorted list : ", array)
#array = [ 0,  3,  6,  7,  8, 13, 21, 28, 36, 41]
isThere = isContainsKey(array, 10)
print("{} is there in {} : {} ".format(10, array, isThere) )