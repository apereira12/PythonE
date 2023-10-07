#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

'''n1 = float(input('Digite a Nota da prova 1:'))
n2 = float(input('Digite a Nota da prova 2:'))
n3 = float(input('Digite a Nota da prova 3:'))
n4 = float(input('Digite a Nota da prova 4:'))
n5 = float(input('Digite a Nota da prova 5:'))
n6 = float(input('Digite a Nota da prova 6:'))
media = (n1+n2+n3+n4+n5+n6)/6
print(f'sua média é: {media:.2f}'''

notas = []

x = int(input('Favor inserir o número de provas: '))
for i in range(x):
    notas.append(float(input(f'Digite a Nota da prova {i+1}:')))
media = sum(notas)/len(notas)
print(f'sua média é: {media:.2f}')

