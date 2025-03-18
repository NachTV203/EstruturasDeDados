# Alocação Dinâmica

**Alocação dinâmica de memória em tempo de execução:**

Alocação dinâmica de memória é o processo de alocação de memória para objetos em tempo de execução, em oposição ao tempo de compilação. Ela permite alocação flexível de memória com base nas necessidades do programa, permitindo que estruturas de dados e objetos cresçam ou diminuam dinamicamente.

Em Python, a alocação dinâmica de memória é gerenciada principalmente por mecanismos como coleta de lixo e contagem de referências. O sistema de gerenciamento de memória do Python manipula automaticamente a alocação e a desalocação de memória no heap, onde residem objetos alocados dinamicamente.

Quando um objeto é criado em Python, a memória é alocada dinamicamente do heap para acomodar os dados e atributos do objeto. A contagem de referência para o objeto é incrementada para rastrear o número de referências a ele. Enquanto houver referências ao objeto, a memória permanece alocada.

Fonte: https://medium.com/@connicet/runtime-vs-compile-time-exploring-memory-allocation-in-python-32bd12acc918
