#Escreva um programa que leia 6 notas diferentes e faça a média do aluno
notas = []

x = int(input('Favor inserir o número de provas: '))
for i in range(x):
    notas.append(float(input(f'Digite a Nota da prova {i+1}:')))
media = sum(notas)/len(notas)
print(f'sua média é: {media:.2f}')

