#Crie um jogo de pedra, papel ou tesoura com o computador. 
#Crie uma variável com uma das opções e pergunte ao utilizador qual a jogada dele. 
#Mostre ao utilizador a escolha do computador e, por fim imprime o resultado comparando com a escolha do utilizador 
#(vitória, e m p a t e ou derrota).

import random
while True:
    usuario_escolha = input("Vamos jogar pedra, papel e tesoura. Você começa, digite a sua eescolha: ").lower()

    opcoes = ['pedra', 'papel', 'tesoura']
    
    computador_escolha = random.choice(opcoes)

    if usuario_escolha == computador_escolha:
        resultado = 'Empate'
    elif (usuario_escolha == 'pedra' and computador_escolha == 'tesoura') or \
        (usuario_escolha == 'papel' and computador_escolha == 'pedra') or \
        (usuario_escolha == 'tesoura' and computador_escolha == 'papel'):
        resultado = 'Você venceu!!!!'
    else:
        resuldado = 'Você perdeu :('

    print ("O computador escolheu: ", computador_escolha)
    print ("Resultado: ", resultado)