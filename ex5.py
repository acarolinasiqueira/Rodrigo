#Crie um programa que pede a idade do utilizador e informa o preço do bilhete de cinema. Se a idade for inferior a 12 anos,
#o bilhete custa 5 euros; se for entre 12 e 18 anos, custa 7 euros; se for superior a 18 anos, custa 10 euros.

while True:
    entrada = input("Para saber quanto pagar nos bilhetes, digite a sua idade: ")
    if entrada.lower() == 'sair':
        break

    idade = int(entrada)
    if idade < 12:
        print("5 euros")
    elif 12 <= idade <= 18:
        print ("7 euros")
    else:
        print ("10 euros")