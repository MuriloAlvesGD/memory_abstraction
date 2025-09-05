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

    def addProcess(self, process):
        
        if self.lastFree >= process.size:
            self.firstFit(self.head, process)
        else:
            self.bestFit(self.head, process, None)
            

    def firstFit(self, prev, process):
        if prev.isEmpty and prev.size >= process.size:
            temp = Node(None, prev.size - process.size)
            prev.next = temp
            prev.process = process
            prev.size = process.size
            prev.isEmpty = False
            self.lastFree -= process.size
        else:
            self.firstFit(prev.next, process)
    
    
    def bestFit(self, prev, process, minor):
        if prev is None:
            if minor is not None:
                self.lastFree = 0
                free = minor.size - process.size

                minor.process = process
                minor.size = process.size
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

        elif prev.size < process.size:
            self.bestFit(prev.next, process, minor)
        
        else:
            if minor is None:
                minor = prev
            
            if prev.size >= minor.size:
                self.bestFit(prev.next, process, minor)
            else:
                self.bestFit(prev.next, process, prev)
            



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
