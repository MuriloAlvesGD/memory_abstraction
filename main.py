import random

class Process:
    size = random.randint(1, 128)

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    totalSize = 128
    freeSize = 128
    firstUse = true
    
    def __init__(self):
        self.head = None

    def addProcess(self, process):
        newNode = Node(process)
        
        if self.head == None:
            self.head = newNode
            
        elif self.firstUse and self.freeSize < process.size:
            self.firstUse = false
        
        elif self.firstUse:
            self.firstFit(self.head, newNode)
            self.freeSize -= process.size
            
        else:
            self.bestFit(self.head, newNode)
       
    def firstFit(prev, node):
        if prev.next == None:
            prev.next = node
        else:
            firstFit(prev.next, node)
            
            
    def bestFit(prev, node):
        
    
    #def worstFit():