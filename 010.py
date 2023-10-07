#Escreva um programa que leia um tipo de dado e usando a função .isnumeric(), retorne ao usuário
dado = input('informe o dado para avaliação: ')
x = (dado).isnumeric()
if x == False:
    print(f'O dado não é numérico')
else:
    print(f'O dado é Numérico')
