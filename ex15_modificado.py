numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verifica qual número é maior e qual é menor para definir o intervalo
if numero1 < numero2:
    menor = numero1
    maior = numero2
else:
    menor = numero2
    maior = numero1

# Imprime os números inteiros no intervalo compreendido entre os dois números
print(f"Os números inteiros entre {menor} e {maior} são:", end=" ")
for i in range(menor + 1, maior):
    print(i, end=" ")
print()  