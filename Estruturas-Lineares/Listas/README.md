Em Python, uma lista é uma estrutura de dados integrada com tamanho dinâmico, capaz de expandir ou reduzir automaticamente conforme necessário. Ela pode armazenar elementos de diferentes tipos, incluindo outras listas, pois, na prática, armazena referências em locais contíguos, enquanto os valores reais podem estar espalhados em diferentes posições na memória.  
As listas permitem a presença de elementos repetidos e são **mutáveis**, ou seja, podem ser alteradas, seja para modificar, substituir ou remover itens. Além disso, são **estruturas ordenadas**, preservando a sequência em que os elementos foram adicionados.  
Os itens de uma lista podem ser acessados diretamente pelo seu índice, começando da posição `0`.

Em Python, as listas não armazenam os valores diretamente dentro de sua estrutura. 
Em vez disso, elas contêm referências (ponteiros) que apontam para os objetos reais na memória.
A própria lista funciona como um contêiner que mantém os endereços de memória dos elementos armazenados. Por exemplo, ao criar uma lista contendo 10, 20, "GfG", 40 e True, o Python aloca esses valores separadamente na memória e armazena seus respectivos endereços dentro da lista.
Isso significa que modificar um item da lista não altera os outros elementos. No entanto, se o objeto referenciado for mutável, como outra lista ou um dicionário, a modificação pode impactar o conteúdo desse objeto.
 Fonte:https://www.geeksforgeeks.org/python-lists/
