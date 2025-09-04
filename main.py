import random

class Process:
    def __init__ (self, i):
        self.size = random.randint(1, 128)
        self.name = f"Process-{i}"

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    totalSize = 128
    freeSize = 128
    
    def __init__(self):
        self.head = None


    def addProcess(self, process):
        newNode = Node(process)
        
        if self.head is None:
            self.head = newNode
            self.freeSize -= process.size
            
        elif self.freeSize >= process.size:
                self.firstFit(self.head, newNode)
                self.freeSize -= process.size
            
        else:
            self.bestFit(self.head, newNode, None)
       
    
    
    def firstFit(self, prev, node):
        if prev.next is None:
            prev.next = node
        else:
            self.firstFit(prev.next, node)
            
            
            
            
    def bestFit(self, prev, node, minor):
        if prev is None:
            if minor is not None:
                self.freeSize += minor.value.size - node.value.size
                minor.value = node.value

        
        elif prev.value.size < node.value.size:
            self.bestFit(prev.next, node, minor)
        
        else:
            if minor is None:
                minor = prev
            
            if prev.value.size >= minor.value.size:
                self.bestFit(prev.next, node, minor)
            else:
                self.bestFit(prev.next, node, prev)
            
    
    #def worstFit():
    
list = LinkedList()
for i in range(4):
    print(f"Espaço livre: {list.freeSize}")
    p = Process(i)
    print (p.name)
    print(f"Tamanho da Inserção: {p.size}")
    list.addProcess(p)
    print(f"Espaço livre após inserção: {list.freeSize}")
    print()
    

print("estado final")
n = list.head
while(n is not None):
    print("--------")
    print(n.value.name)
    print(n.value.size)
    n = n.next