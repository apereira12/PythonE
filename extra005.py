#Jogo da Adivinhação
#Escolha um número aleatório entre 1 e 10, depois peça ao usuário para adivinhar o número.

import random

aleatorioMaquina=int(random.randrange (1,10))

escolhaUsuario = int(input('Favor informar seu número de 1 à 10: '))

def verifica():
    if escolhaUsuario>10 or escolhaUsuario<1:
        return print('Escolha um número de 1 à 10')
    elif aleatorioMaquina==escolhaUsuario:
        print('Você adivinhou o número')
    else:
        print('Você errou o número')

print(f'a escolha da máquina foi {aleatorioMaquina}')
print(f'a sua escolha foi {escolhaUsuario}')
verifica()