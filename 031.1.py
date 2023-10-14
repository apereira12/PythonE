# Escreva um programa que verifique se uma frase é um palíndromo.

print('-------- Programa de verificação palíndromo --------')
frase = input('Escreva aqui sua frase:')

'''for i in range(len(frase)//2):
    if frase[i] != frase[-i - 1]:
        print('Não é um palíndromo')
    else:
        print('É um palíndromo')
'''
compatibilidade = 0
for i in range(0,len(frase)):

    if frase[i] == frase[-i - 1]:
        compatibilidade= compatibilidade + 1
if compatibilidade == len(frase):
    print('É um palíndromo')
else:
    print('Não é palíndromo')



