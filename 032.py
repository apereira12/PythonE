#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

n1 = int(input('Favor informar o N1:'))
n2 = int(input('Favor informar o N2:'))
if n1 % 2 != 0:
    n1 = n1+1
else:
     n1 = n1

for i in range(n1, n2 + 1, 2):
    print(i)

