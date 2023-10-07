#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random

opcoes = ('pedra','papel','tesoura')
escolhamaquina = random.choice(opcoes)
suaescolha = input('Escolha pedra, papel, tesoura: ')
print(escolhamaquina)
def jokenpo():
    if escolhamaquina == suaescolha:
        return 'Temos um empate'
    elif escolhamaquina == 'pedra' and suaescolha == 'tesoura':
        return 'A máquina vence'
    elif escolhamaquina == 'papel' and suaescolha == 'pedra':
        return 'A máquina vence'
    elif escolhamaquina == 'tesoura' and suaescolha == 'papel':
        return 'A máquina vence'
    else:
        return 'Você vence'

print(jokenpo())


