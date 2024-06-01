letra = input ("Escolha uma letra: ")
vogais=["a" , "e" , "i" , "o" , "u"]
if letra in vogais:
    print ("Vogal")
else:
    print("Consoante")

#ou

entrada = input("Escolha uma letra ou digite um inteiro: ")

# Verifica se a entrada é uma letra vogal
if entrada.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vogal")
# Verifica se a entrada é uma consoante
elif entrada.isalpha():
    print("Consoante")
# Verifica se a entrada é um dígito
elif entrada.isdigit():
    print("Você digitou um inteiro. Por favor, insira uma letra.")
# Se a entrada não for uma letra ou um dígito
else:
    print("Entrada inválida. Por favor, insira uma letra ou um inteiro.")

#ou

entrada = input("Escolha uma letra ou digite um inteiro: ")

if entrada.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vogal")
elif entrada.isalpha():
    print("Consoante")
else:
    print("Você digitou um inteiro ou uma entrada inválida. Por favor, insira uma letra.")
