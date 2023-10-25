#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

numero = int(input('Insira o número que você quer saber a tabuada:'))
for i in range(1,11):
    print(f'|{numero}   x    {i} = {numero*i} |')


