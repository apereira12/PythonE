'''Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos
'''
media = 0
soma_idades = 0
for i in range(2):
    nome = input('Favor digitar o nome:')
    idade = int(input('Favor digitar a idade:'))
    soma_idades += idade
    media = soma_idades/4
    sexo = input('Favor informar o sexo: ').lower()



print(idade)



