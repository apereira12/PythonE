#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

def VerificaPar():
    numero = float(input('Informe o Número: '))
    if numero%2 ==0:
        print('Esse Número é par')
    else:
        print('Esse Número é impar')


VerificaPar()

