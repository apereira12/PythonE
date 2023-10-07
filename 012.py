
'''Crie um programa que leia um nome, e mostre o primeiro e o último nome'''
nome = input('Insira seu nome: ').strip()

nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e o último é {nome[-1]}')