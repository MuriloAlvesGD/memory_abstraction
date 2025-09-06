import random
from prettytable import PrettyTable

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
    freeSize = 128
    useBest = True
    useFirst = True
    
    def __init__(self):
        self.head = Node(None, 128)

    def calcNodeSize(self, process):
        if process.size%2 == 0:
            return process.size
        else:
            return process.size + 1

    def addProcess(self, process):
        
        if self.freeSize >= process.size and self.useFirst:
            self.firstFit(self.head, process)
        elif self.useBest:
            self.bestFit(self.head, process, None)
            self.useBest = False
            self.useFirst = False
        else:
            self.worstFit(self.head, process, None)
        


    def firstFit(self, node, process):
        if node.isEmpty and node.size >= process.size:
            newNodeSize = self.calcNodeSize(process)
            temp = Node(None, node.size - newNodeSize)
            node.next = temp
            node.process = process
            node.size = newNodeSize
            node.isEmpty = False
            self.freeSize -= newNodeSize
            
            print("+--------------------------------+")
            print("|     TENTATIVA DE INSERÇÃO      |")
            print("+--------------------------------+")  
            print("| SUCESSO | FIRST FIT |")
            print("+---------+-----------+")
        else:
            self.firstFit(node.next, process)
    
    
    def bestFit(self, node, process, minor):
        if node is None:
            if minor is not None:
                tempLog = Process(0)
                tempLog.name = minor.process.name
                tempLog.size = minor.process.size
                
                newNodeSize = self.calcNodeSize(process)
                free = minor.size - newNodeSize
                self.freeSize += free

                minor.process = process
                minor.size = newNodeSize
                minor.isEmpty = False
                
                print("+-----------+")
                print("| REMOVENDO |")
                tabela = PrettyTable()
                tabela.field_names = ["PROCESSO", "TAMANHO DO PROCESSO", "TAMANHO DO NÓ"]
                tabela.add_row([f"{tempLog.name}", f"{tempLog.size}KB", f"{self.calcNodeSize(tempLog)}KB"])
                print(tabela)

                print("+--------------------------------+")
                print("|     TENTATIVA DE INSERÇÃO      |")
                print("+--------------------------------+")  
                print("| SUCESSO | BEST FIT |")
                print("+---------+----------+")
                
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
            else:
                print("+--------------------------------+")
                print("|     TENTATIVA DE INSERÇÃO      |")
                print("+--------------------------------+")  
                print("| FALHA NA INSERÇÃO |")
                print("+-------------------+")            

        elif node.size < process.size:
            self.bestFit(node.next, process, minor)
        
        else:
            if minor is None:
                minor = node
            
            if node.size >= minor.size:
                self.bestFit(node.next, process, minor)
            else:
                self.bestFit(node.next, process, node)
    
    def worstFit(self, node, process, biggest):
        if node is None:
            if biggest is not None:
                newNodeSize = self.calcNodeSize(process)
                free = biggest.size - newNodeSize
                self.freeSize += free

                biggest.process = process
                biggest.size = newNodeSize
                biggest.isEmpty = False
                print("+--------------------------------+")
                print("|     TENTATIVA DE INSERÇÃO      |")
                print("+--------------------------------+")  
                print("| SUCESSO | WORST FIT |")
                print("+---------+-----------+")

                if free > 0:
                    if biggest.next is None:
                        temp = Node(None, free)
                        temp.next = biggest.next
                        biggest.next = temp

                    elif biggest.next.isEmpty:
                        biggest.next.size += free
                    else:
                        temp = Node(None, free)
                        temp.next = biggest.next
                        biggest.next = temp
            else:
                print("+--------------------------------+")
                print("|     TENTATIVA DE INSERÇÃO      |")
                print("+--------------------------------+")  
                print("| CHAMADA DE WORST PARA BEST FIT |")
                print("+--------------------------------+")
                self.bestFit(self.head, process, None)
            

        elif node.size < process.size:
            self.worstFit(node.next, process, biggest)
        
        else:
            if biggest is None and node.isEmpty:
                biggest = node
            
            if node.isEmpty and node.size > biggest.size:
                self.worstFit(node.next, process, node)
            else:
                self.worstFit(node.next, process, biggest)
                
    def printList(self):
        node = self.head
        
        tabela = PrettyTable()
        tabela.field_names = ["NÓ", "TAMANHO DO NÓ", "PROCESSO", "TAMANHO DO PROCESSO"]
        while(node is not None):
            if node.isEmpty:
                row = [f"{hex(id(node))}", f"{node.size}KB", "----", "0KB"]
            else:
                row = [f"{hex(id(node))}", f"{node.size}KB", f"{node.process.name}", f"{node.process.size}KB"]
            tabela.add_row(row)
            node = node.next
        print(tabela)



list = LinkedList()

numero = int(input("Digite a quantidade de processos para a simulação: "))
print()
print()
for i in range(numero):
    tabela = PrettyTable()
    print("+-----------------+")
    print(f"| {i+1}# ADICIONANDO |")
    tabela.field_names = ["PROCESSO", "TAMANHO DO PROCESSO"]
    p = Process(i+1)
    tabela.add_row([f"{p.name}", f"{p.size}KB"])
    print(tabela)
    print()
    list.addProcess(p)
    print()
    print("+-------------------------+")
    print("| ESTADO ATUAL DA MEMÓRIA |")
    list.printList()
    print()
    print()
    print()
    
print("+---------------------------+")
print("|  ESTADO FINAL DA MEMÓRIA  |")
list.printList()
