#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

peso = 0
peso_menor = 0
peso_maior = 0


for i in range(0,7):
    peso = float(input('Favor informar seu peso:'))

    if peso < peso_menor or i ==0:
        peso_menor = peso
    if peso > peso_maior:
        peso_maior = peso


print(f'o menor peso é {peso_menor} e o maior peso é {peso_maior}')
