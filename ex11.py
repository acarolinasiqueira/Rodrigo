# Pede ao utilizador para inserir um número e imprima a tabuada desse número de 1a 10

numero = int(input("Insira um número diferente de zero: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
