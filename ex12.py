numero = int(input("Escolha um número aleatório: "))

if numero < 0:
    print("Por favor, escolha um número positivo.")
else:
    for i in range(0, numero + 1):
        print (i)

