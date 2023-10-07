#Escreva um programa que peça ao usuário um número de 1 a 7
# e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

def dia_semana(numero):

    DiaSemanal = ['SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÁBADO', 'DOMINGO']
    return DiaSemanal[numero - 1]

numero = int(input('Insira um número de 1 a 7: '))
print(dia_semana(numero))


''' DiaSemanal = {1:'SEGUNDA', 2:'TERÇA', 3:'QUARTA', 4:'QUINTA', 5:'SEXTA', 6:'SÁBADO', 7:'DOMINGO'}
    return DiaSemanal.get(numero, 'Valor inválido')


numero = int(input('Insira um número de 1 a 7: '))
print(dia_semana(numero))'''


