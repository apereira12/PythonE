#Escreva um programa que verifique se uma frase é um palíndromo. Faça usando apenas For
frase = input('Escreva aqui sua frase:')

lista = []
for i in frase:
    lista.append(i)
print(lista)

lista1 = lista[::-1]

if lista == lista1:
    print('é um palíndromo')
else:
    print('Não é um palíndromo')

