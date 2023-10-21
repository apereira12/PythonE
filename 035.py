'''Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos
'''
media = 0
soma_idades = 0
mulher_abaixo=0
idade_homem = 0
nome_homem = 'Nenhum homem informado'
for i in range(2):
    nome = input('Favor digitar o nome:')
    idade = int(input('Favor digitar a idade:'))
    soma_idades += idade
    sexo = input('Favor informar o sexo: (H= Homem, M = Mulher').lower()

    if sexo=="H" and idade > idade_homem:
        idade_homem=idade
        nome_homem = nome
    if sexo =="M" and idade<20:
        mulher_abaixo+=1






media = soma_idades/2
print(f'a média de idade é {media}')

print(f'o homem mais velho é: {nome_homem}')
print(f'a quatidade de mulheres abaixo de 20 anos é {mulher_abaixo}')


