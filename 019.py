#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10,
# entre 10 e 20 ou maior que 20.

def numero(valor):
    if valor < 10:
        print("Menor que 10")
    elif valor >= 10 and valor <= 20:
        print("Entre 10 e 20")
    else:
        print('Maior que 20')


valor = int(input('Favor digitar o  número: '))

numero(valor)


