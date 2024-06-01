#Peça ao utilizador para inserir um número e faça uma contagem regressiva até zero.
numero = int(input("Escolha um número aleatório: "))

if numero < 0:
    print("Por favor, escolha um número positivo.")
else:
    for i in range(numero, -1, -1):
        print (i)
