'''Crie um programa que leia o Nome completo de uma pessoa e mostre:
O Nome com todas as letras maiúsculas
O Nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro Nome'''


Nome = input('Insira seu Nome: ').strip()
NomeMaiusculo = Nome.upper()


NomeMinusculo = Nome.lower()

NomeSemEspaco = Nome.replace(' ','')

Nome = Nome.split()




print(f'Seu primeiro Nome é {Nome[0]} e ele tem {len(Nome[0])}'
      f'\n Seu Nome maiusculo {NomeMaiusculo}'
      f'\n Seu Nome minusculo {NomeMinusculo}'
      f'\n Seu nome tem {len(NomeSemEspaco)} letras')
