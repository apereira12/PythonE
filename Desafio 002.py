'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome

OBS: Tratar os espaços extras entre os nomes'''

nome = input('Insira seu nome: ')
nome = nome.upper()
print(nome)

nome = nome.lower()
print(nome)
nome.strip()
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])}')
nome = ''.join(nome)
print(f'Seu nome tem {len(nome)} letras')

