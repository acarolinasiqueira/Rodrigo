#Solicite um número ao utilizador e calcula a soma dos números pares de 1até ao número inserido.

numero = int(input("Escolha um número e digite aqui: "))

soma = 0
a = []    

for i in range (0, numero +1, 2):
    soma += i
    a.append(str(i))
    
numeros_pares = ', '.join(a)

print("Números pares:", numeros_pares)
print("Soma dos números pares:", soma)

########################################################################################################################################

numero = int(input("Escolha um número e digite aqui: "))

if numero < 0:
    print("Por favor, escolha um número positivo.")
else:
    numeros_pares = ', '.join([str(i) for i in range(0, numero + 1, 2)])
    soma = sum(range(0, numero + 1, 2))

    print("Números pares:", numeros_pares)
    print("Soma dos números pares:", soma)