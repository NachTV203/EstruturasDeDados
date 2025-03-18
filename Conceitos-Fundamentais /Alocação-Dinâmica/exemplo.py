def create_dynamic_list(n):
dynamic_list = []
para i em intervalo(n):
dynamic_list.append(i)
retornar dynamic_list

# Tempo de execução
n = int(input(“Digite o número de elementos: “))
my_list = create_dynamic_list(n)

# Tempo de compilação
print(“Comprimento da lista:”, len(my_list))
