# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:42:24 2019

@author: suman
"""
import queue

class Node:
    
    def __init__(self, id):
        self.id = id
        self.adjucent = []
    
    def __str__(self):
        return str(self.id)
    
class Graph:
    
    def __init__(self):
        self.graph = {}
        #self.visited_set = set()
        
    def createVertex(self, id):
        node = Node(id)
        self.graph[id] = node
        
    def getNode(self, id):
        return self.graph[id]
    
    def addEdge(self, sourceId, destinationId):
        source = self.graph[sourceId] 
        destination = self.graph[destinationId] 
        source.adjucent.append(destination)
        print(self.graph[sourceId], self.graph[sourceId].adjucent)
        
    def hasPathDFS(self, sourceId , destinationId):
        node_source = self.graph[sourceId]
        node_destination = self.graph[destinationId]
        visited_set = set()
        return self.containsPathDFS(visited_set, node_source, node_destination)
    
    def containsPathDFS(self, isVisistedSet, source, destination):
        
        if(source.id == destination.id):
            return True
        
        if source in isVisistedSet:
            return False
        
        isVisistedSet.add(source)
        for child in source.adjucent:
            if self.containsPathDFS(isVisistedSet, child, destination):
                return True
        
        return False
    
    def hasPathBFS(self, sourceId , destinationId):
        node_source = self.graph[sourceId]
        node_destination = self.graph[destinationId]
        visited_set = set()
        nextToVisit = queue.Queue()
        #nextToVisit.put(node_source)
        #nextToVisit = queue.Queue([node_source])
        return self.containsPathBFS(nextToVisit, visited_set, node_source, node_destination)
    
    def containsPathBFS(self, nextToVisit, isVisistedSet, source, destination):
        if source in  isVisistedSet:
            return False
        
        isVisistedSet.add(source)
        if source == destination:
            return True
         
            
        for child in source.adjucent:
            nextToVisit.put(child)
            
        if not nextToVisit.empty():
            next_node = nextToVisit.get()
            if self.containsPathBFS(nextToVisit, isVisistedSet, next_node, destination):
                return True
        
        return False
    
# =============================================================================
#     def containsPathBFS(self, source, destination):
#         nextToVisit = queue.Queue()
#         nextToVisit.put(source)
#         isVisistedSet = set()
#         
#         while not nextToVisit.empty():
#             source = nextToVisit.get()
#             if source in  isVisistedSet:
#                 return False
#             
#             isVisistedSet.add(source)
#             if source == destination:
#                 return True
#             
#             #for child in source.adjucent:
#                 #nextToVisit.append(child)
#             nextToVisit.extend(source.adjucent)
#         
#         return False
# =============================================================================
        
if __name__ == '__main__':
    g = Graph()
    g.createVertex(0)
    g.createVertex(1)
    g.createVertex(2)
    g.createVertex(3)
    g.createVertex(4)
    g.createVertex(5)
    g.createVertex(6)
     
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(2, 3)     
    g.addEdge(2, 4)     
    g.addEdge(4, 5)     
    g.addEdge(4, 6)     
    
    print(g.hasPathDFS(2, 6)) 
    print(g.hasPathDFS(0, 6))
    print(g.hasPathDFS(1, 6))

    print(g.hasPathBFS(2, 6)) 
    print(g.hasPathBFS(0, 6))
    print(g.hasPathBFS(1, 6))    
        
        