#Crie um programa que peça para o utilizador inserir dois números, e se ele quer realizar a operação de adição ou de subtração. 
#A partir desta escolha, mostre o resultado na tela.

entrada = input("Digite dois números separados por um espaço e depois diga o tipo de operação 'adição ou subtração' que deseja fazer entre eles: ")

numero_1_str, numero_2_str, operacao = entrada.split()

numero_1 = int(numero_1_str)
numero_2 = int(numero_2_str)

if operacao.lower() == 'adição':
    resultado = numero_1 + numero_2
    print ("O resultado da adição é: ", resultado)
elif operacao.lower() == 'subtração':
    resultado = numero_1 - numero_2
    print ("O resultado da subtração é: ", resultado)
else: 
    print("Operação inválida. Por favor, escolha 'adição' ou 'subtração'.")
