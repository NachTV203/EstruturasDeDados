# Variável global (alocação estática)
a = 0

def incrementa():
    global a  # Referência à variável global
    b = 0  # Variável local (alocação automática)
    
    # Variável local com comportamento de alocação estática
    if not hasattr(incrementa, "c"):
        incrementa.c = 0  # Inicializa apenas uma vez
    
    print(f"a: {a}, b: {b}, c: {incrementa.c}")
    
    a += 1
    b += 1
    incrementa.c += 1

# Loop principal
for _ in range(5):
    incrementa()

#codigo criado utilizando a ide Cursor Ai
