#Exemplo simples de fila usando Python

#Criando uma fila vazia
fila = []

#Adicionando elementos na fila (enfileirar)

print("Adicionando elementos na fila:")

fila.append("João")
print(f"Adicionou: João")

fila.append("Maria") 
print(f"Adicionou: Maria")

fila.append("Pedro")
print(f"Adicionou: Pedro")

print(f"\nFila atual: {fila}")
print(f"Tamanho da fila: {len(fila)}")

#Removendo elementos da fila (desenfileirar)

print("\nRemovendo elementos da fila:")

primeiro = fila.pop(0)  # Remove e retorna o primeiro elemento
print(f"Removeu: {primeiro}")

segundo = fila.pop(0)
print(f"Removeu: {segundo}")

terceiro = fila.pop(0)
print(f"Removeu: {terceiro}")

print(f"\nFila vazia: {fila}")

