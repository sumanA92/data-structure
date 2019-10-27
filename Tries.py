# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 01:00:48 2019

@author: suman
"""

class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        
# =============================================================================
#     def __init__(self):
#         self.children = {}
#         self.isEndOfWord = False        
# =============================================================================
        
class Trie:

    def __init__(self):
        self.root = self.createNode()

    def createNode(self):
        return TrieNode()

    def insert(self, key):
        prefix_node = self.root
        for level in range(len(key)):
            index = self._charToIndex(key[level])
            
            if not prefix_node.children[index]:
                prefix_node.children[index] = self.createNode()
            prefix_node = prefix_node.children[index]
            
        prefix_node.isEndOfWord = True
    
# =============================================================================
#     def insert(self, key):
#         prefix_node = self.root
#         for char_key in key:
#             
#             if not prefix_node.children.get(char_key):
#                 prefix_node.children[char_key] = self.createNode()
#             prefix_node = prefix_node.children[char_key]
#             
#         prefix_node.isEndOfWord = True
# =============================================================================
        
    def search(self, key):
        prefix_node = self.root
        for char_key in key:
            index = self._charToIndex(char_key)
            
            if not prefix_node.children[index]:
                return False
            prefix_node = prefix_node.children[index]
                
        return prefix_node != None and prefix_node.isEndOfWord
  
    def _charToIndex(self, ch):
        return ord(ch) - ord('a')
    
def main():
    keys = ['the', 'a', 'there', 'answer', 'any', 'love']
    output = ['Not present in trie', 'Present in trie']
    
    t = Trie()
    
    for key in keys:
        t.insert(key)
        
    print('{}........{}'.format('the',output[t.search('the')]))     
    print('{}........{}'.format('rose',output[t.search('rose')]))     
    print('{}........{}'.format('The',output[t.search('The')]))
        
if __name__ == '__main__':
    main()            
