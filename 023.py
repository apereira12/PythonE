#Escreva um programa que peça ao usuário
# uma palavra e imprima se começa com vogal ou consoante.

def TestaVogal(frase):
    vogal = ['a', 'e', 'i', 'o', 'u']
    if(frase in vogal):
            print('Essa frase começa com uma vogal')
    else:
        print('Essa frase não começa com uma vogal')
frase = input('Favor digitar uma frase: ').lower()[0]

TestaVogal(frase)