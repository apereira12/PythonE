#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).

def idade(x):
    if x >= 18:
        print('Você já pode ser preso')
    else:
        print('Você ainda pode cometer crimes')

x= int(input('Favor informar a idade:'))
idade(x)