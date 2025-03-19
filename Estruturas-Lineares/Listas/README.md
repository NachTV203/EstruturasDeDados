# Listas 

Em **Python**, uma **lista** é uma **estrutura de dados dinâmica**, capaz de **expandir ou reduzir automaticamente** conforme necessário. Ela pode armazenar **elementos de diferentes tipos**, incluindo **outras listas**, pois, na prática, armazena **referências** em locais contíguos, enquanto os valores reais podem estar espalhados em diferentes posições na memória.  

## 📌 Características das Listas  
- **Mutáveis**: As listas podem ser **alteradas**, permitindo modificar, substituir ou remover itens.  
- **Ordenadas**: As listas **preservam a sequência** em que os elementos foram adicionados.  
- **Acesso por índice**: Os itens de uma lista podem ser acessados **diretamente pelo índice**, começando da posição `0`.  
- **Permite elementos repetidos**: Uma lista pode conter **elementos duplicados**.

## 📌 Armazenamento de Dados em Listas  

Em Python, as listas **não armazenam os valores diretamente** dentro de sua estrutura. Em vez disso, elas **contêm referências (ponteiros)** que apontam para os objetos reais na memória.  

![image](https://github.com/user-attachments/assets/16b4e617-2f54-4821-ab55-d5b91eae48b8)

A própria lista funciona como um **contêiner** que mantém os **endereços de memória** dos elementos armazenados. Por exemplo, ao criar uma lista contendo os valores:  
`[10, 20, "GfG", 40, True]`, o Python **aloca esses valores separadamente** na memória e armazena seus respectivos endereços dentro da lista.  

Isso significa que **modificar um item da lista** não altera os outros elementos. No entanto, se o **objeto referenciado for mutável**, como outra lista ou um dicionário, a modificação pode impactar o conteúdo desse objeto.  

***Fonte:*** https://www.geeksforgeeks.org/python-lists/
