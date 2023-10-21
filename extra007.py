#Calculadora de IMC
#Solicite ao usuário sua altura e peso, e calcule seu Índice de Massa Corporal (IMC).


'''Menor que 18,5	Magreza
18,5 a 24,9	Normal
25 a 29,9	Sobrepeso
30 a 34,9	Obesidade grau I
35 a 39,9	Obesidade grau II
Maior que 40	Obesidade grau III'''
peso = float(input('Favor informar seu peso: '))
altura = float(input('Favor informar sua altura: '))
calcularimc = peso/(altura*altura)
def imc():
    if calcularimc<18.5:
        print('Baixo peso')
    elif calcularimc>=18.5 and calcularimc<=24.9:
        print('Peso normal')
    elif calcularimc>=25 and calcularimc<=29.9:
        print('Sobrepeso')
    elif  calcularimc>=30 and calcularimc<=34.9:
        print('Obesidade grau I')
    elif  calcularimc>=35 and calcularimc<=39.9:
        print('Obesidade grau II')
    else:
        print('Obesidade grau III')



imc()