#Exemplo de árvore (estruturas não linear)

class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []  #Lista para armazenar os filhos do nó

#Criando os nós da árvore
raiz = No(10)  #Raiz da árvore
n1 = No(20)    #Filho 1
n2 = No(30)    #Filho 2
n3 = No(40)    #Filho 3

#Conectando os filhos à raiz
raiz.filhos.append(n1)
raiz.filhos.append(n2)
n1.filhos.append(n3)  #n3 é filho de n1

#Vamos acessar os valores na árvore
print(raiz.valor)         #A raiz tem o valor 10
print(raiz.filhos[0].valor)  #O primeiro filho da raiz tem o valor 20
print(raiz.filhos[0].filhos[0].valor)  #O filho de n1 tem o valor 40

#A árvore ficaria assim:
#          10
#        /    \
#      20      30
#     /
#    40
