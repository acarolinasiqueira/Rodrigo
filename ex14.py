#Gere um número aleatório entre 1e 20 e permita que o utilizador adivinhe. 
# Dê dicas se o palpite foi muito alto ou muito baixo. Continue até que o utilizador acerte.

# while true
# import randon
# escolha_computador
# escolha_usuario

import random

computador_escolha = random.randint(0, 50)

while True:
    usuario_escolha = int(input("Tente adivinhar o número em que estou pensando, entre 0 e 50!: "))
    
    if usuario_escolha < computador_escolha:
        resultado = 'Um pouco mais!'
    elif usuario_escolha > computador_escolha:
        resultado = 'Um pouco menos!'
    elif usuario_escolha == computador_escolha:
        resultado = 'Eita, você acertou!!!'
    else:
        resultado = ' invalido'
        break 
    
    print(resultado)


import random

computador_escolha = random.randint(0, 50)

frases = [
    'Um pouco mais!',
    'Um pouco menos!',
    'Tente novamente!',
    'Quase lá!',
    'Não desista!',
    'Você consegue!',
    'Continue tentando!',
    'A próxima será!',
]

while True:
    usuario_escolha = input("Tente adivinhar o número em que estou pensando, entre 0 e 50!: ")
    
    if not usuario_escolha.isdigit():
        print("Por favor, insira um número inteiro válido.")
        continue
    
    usuario_escolha = int(usuario_escolha)
    
    diferenca = abs(computador_escolha - usuario_escolha)
    
    if usuario_escolha < computador_escolha:
        resultado = random.choice(frases)
    elif usuario_escolha > computador_escolha:
        resultado = random.choice(frases)
    elif usuario_escolha == computador_escolha:
        resultado = 'Eita, você acertou!!!'
        break
    elif diferenca == computador_escolha**2:
        resultado = 'Talvez o quadrado desse...'
    else:
        resultado = 'Você está longe!'
    
    print(resultado)