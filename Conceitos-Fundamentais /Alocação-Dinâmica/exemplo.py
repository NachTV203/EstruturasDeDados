def criar_lista_dinamica(n):
    
    lista_dinamica = []
    
    for i in range(n):
        lista_dinamica.append(i)
        
    return lista_dinamica

# Tempo de execução (Runtime)
n = int(input("Digite o número de elementos: "))
minha_lista = criar_lista_dinamica(n)

# Tempo de compilação (Compile Time)
print("Tamanho da lista:", len(minha_lista))
