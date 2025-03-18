n = int(input("Digite o número de elementos: "))

def create_dynamic_list():
    global n  
    dynamic_list = []  

    
    if not hasattr(create_dynamic_list, "count"):
        create_dynamic_list.count = 0 

    for i in range(n):
        dynamic_list.append(i)

    print(f"Execução {create_dynamic_list.count + 1}: Lista criada com {len(dynamic_list)} elementos")
    
    create_dynamic_list.count += 1 

    return dynamic_list

for _ in range(3):
    my_list = create_dynamic_list()
  
