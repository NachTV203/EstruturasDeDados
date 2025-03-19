# Alocação Estática

## O que é alocação estática?

A **alocação estática** de memória é um conceito importante na programação, especialmente no **gerenciamento de memória**. Ela se refere à alocação de memória **durante o tempo de compilação**, onde o **tamanho** e a **localização** das variáveis são **definidos antes da execução do programa**. Isso contrasta com a **alocação dinâmica**, onde a memória é alocada **em tempo de execução**.

## Como funciona a alocação estática?

A **alocação estática** ocorre em dois casos principais:

- **Variáveis globais**: declaradas fora de funções e disponíveis durante toda a execução do programa.
- **Variáveis locais estáticas**: declaradas dentro de funções usando o modificador `static`, permitindo que **mantenham seu valor** durante toda a vida do programa, **mesmo após a função ser chamada várias vezes**.

## Onde as variáveis estáticas são armazenadas?

Variáveis **globais** ou **estáticas** são geralmente alocadas na **seção de dados (Data Segment)** da memória do programa.


***Fonte: Universidade Federal do paraná,*** https://www.inf.ufpr.br/hexsel/ci067/10_aloc.html 

