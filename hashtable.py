# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:35:18 2019

@author: suman
"""

class HashTable:
    
    def __init__(self):
        self.hash_list = [[] for _ in range(10)]
        
    def isEmpty(self):
        #len(list) == 0, if list ==[] , if not list
        return  bool(self.hash_list)

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_list)  
        key_exists = False
        bucket = self.hash_list[hash_key]
        
        for i,kv in enumerate(bucket):
            k, v = kv
            if key ==  k:
                key_exists = True
                break
       
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))
        
    
    def search(self, key):
        hash_key = hash(key) % len(self.hash_list)  
        bucket = self.hash_list[hash_key]
        
        for i,kv in enumerate(bucket):
            k, v = kv
            if key ==  k:
                return v

    def delete(self, key):
        hash_key = hash(key) % len(self.hash_list)  
        bucket = self.hash_list[hash_key]
        
        for i,kv in enumerate(bucket):
            k, v = kv
            if key ==  k:
                del bucket[i]
                print('{} key deleted'.format(key))
                return
        print('{} key not found'.format(key))    
 
    def __str__(self):
           attrs = vars(hash_table)#works only for dict
           return ', '.join("%s: %s" % item for item in attrs.items())
           
if __name__  == '__main__':
    hash_table = HashTable()
    print(hash_table.isEmpty())
    hash_table.insert('A','Apple')
    print(hash_table)
    print(hash_table.search('A'))
    print(hash_table.search('B'))
    hash_table.delete('A')
    hash_table.delete('A')
    