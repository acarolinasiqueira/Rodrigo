#Cria um programa que peça ao utilizador para inserir três números inteiros e, imprima na consola o maior número.

while True:
    entrada = input("Digete três números diferentes semprados por espaço. ")
    if entrada.lower() == 'sair':
        break 

    numero_1_str, numero_2_str, numero_3_str = entrada.split()
    numero_1 = int(numero_1_str)
    numero_2 = int(numero_2_str)
    numero_3 = int(numero_3_str)

    maior_numero = max(numero_1, numero_2, numero_3)

    print("O maior número é o: ", maior_numero)
####################################################################################################################################
while True:
    entrada = input("Digite três números diferentes separados por espaço ou digite 'sair' para terminar: ")
    if entrada.lower() == 'sair':
        break 
    
    numero_1_str, numero_2_str, numero_3_str = entrada.split()
    numero_1 = int(numero_1_str)
    numero_2 = int(numero_2_str)
    numero_3 = int(numero_3_str)

    maior_numero = max(numero_1, numero_2, numero_3)

    print("O maior número é o:", maior_numero)
