#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

def TestaVogal(letra):
    vogal = ['a', 'e', 'i', 'o', 'u']
    if(letra in vogal):
            print('Essa letra é uma vogal')
    else:
        print('Essa letra não é uma vogal')
letra = input('Favor digitar uma letra: ').lower()

TestaVogal(letra)




