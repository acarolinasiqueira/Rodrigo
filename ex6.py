# Cria um programa que peça ao utilizador para inserir o peso (em kg) e a altura (em metros) que determine se a pessoa está abaixo
#do peso, com peso normal, com sobrepeso, ou obesa, com base no Índice de Massa Corporal (IMC). IMC =peso/(altura*altura)

# Solicita ao usuário para inserir o peso e a altura separados por espaço
# Divide a entrada do usuário em duas partes usando o método split()
# Converte as partes para float

while True:
    entrada = input("Insira o seu peso (em kg) e altura (em metros), separados por espaço: ")
    if entrada.lower() == 'sair':
        break 
    peso_str, altura_str = entrada.split()

    peso = float(peso_str)
    altura = float(altura_str)

    imc = peso / (altura * altura)

    if imc < 18.5:
        categoria = "abaixo do peso"
    elif 18.5 <= imc < 25:
        categoria = "com peso normal"
    elif 25 <= imc < 30:
        categoria = "com sobrepeso"
    else:
        categoria = "obesa"

    print("O seu IMC é:", imc)
    print("Você está", categoria)
