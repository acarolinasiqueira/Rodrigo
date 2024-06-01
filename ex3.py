numero = int(input("Escolha um número entre 1 e 100. "))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")


#loop

while True:
    entrada = input("Digite um número de 1 a 100, e se desejar sair do jogo digite 'sair': ")
    if entrada.lower() == 'sair':
        break

    numero = int(entrada)
    if numero % 2 == 0:
        print("Par")
    else: 
        print("Ímpar")