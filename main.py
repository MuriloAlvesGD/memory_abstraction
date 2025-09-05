import random

class Process:
    def __init__ (self, i):
        self.size = random.randint(1, 128)
        self.name = f"Process-{i}"

class Node:
    def __init__ (self, process, size):
        self.next = None

        if process is None:
            self.isEmpty = True
            self.size = size
        else:
            self.process = process
            self.size = process.size
            self.isEmpty = False


class LinkedList:
    lastFree = 128
    
    def __init__(self):
        self.head = Node(None, 128)

    def calcNodeSize(self, process):
        if process.size%2 == 0:
            return process.size
        else:
            return process.size + 1

    def addProcess(self, process):
        
        if self.lastFree >= process.size:
            self.firstFit(self.head, process)
        else:
            self.bestFit(self.head, process, None)


    def firstFit(self, node, process):
        if node.isEmpty and node.size >= process.size:
            newNodeSize = self.calcNodeSize(process)
            temp = Node(None, node.size - newNodeSize)
            node.next = temp
            node.process = process
            node.size = newNodeSize
            node.isEmpty = False
            self.lastFree -= newNodeSize
        else:
            self.firstFit(node.next, process)
    
    
    def bestFit(self, node, process, minor):
        if node is None:
            if minor is not None:
                self.lastFree = 0
                newNodeSize = self.calcNodeSize(process)
                free = minor.size - newNodeSize

                minor.process = process
                minor.size = newNodeSize
                minor.isEmpty = False

                if free > 0:
                    if minor.next is None:
                        temp = Node(None, free)
                        temp.next = minor.next
                        minor.next = temp

                    elif minor.next.isEmpty:
                        minor.next.size += free
                    else:
                        temp = Node(None, free)
                        temp.next = minor.next
                        minor.next = temp

        elif node.size < process.size:
            self.bestFit(node.next, process, minor)
        
        else:
            if minor is None:
                minor = node
            
            if node.size >= minor.size:
                self.bestFit(node.next, process, minor)
            else:
                self.bestFit(node.next, process, node)
            



list = LinkedList()
for i in range(4):
    print(f"Espaço livre: {list.lastFree}")
    p = Process(i)
    print (p.name)
    print(f"Tamanho da Inserção: {p.size}")
    list.addProcess(p)
    print(f"Espaço livre após inserção: {list.lastFree}")
    print()
    

print("ESTADO FINAL")
print("--------")
print("cabeça")
n = list.head
while(n is not None):
    print(f"Está livre: {n.isEmpty}")
    if not n.isEmpty:
        print(f"Alocado por: {n.process.name}")
    print(f"Tamanho: {n.size}")
    print("--vvv--")
    n = n.next
