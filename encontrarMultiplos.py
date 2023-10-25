#Escreva um programa que calcule a soma de todos os números múltiplos de x que são encontrados entre 1 até y

soma =  0
x = int(input('Favor inserir o número que você deseja que seja encontrados os múltiplos:' ))
y = int(input('Favor inserir o range final para encontrar os múltiplos:' ))
for i in range(1,y):
    if i %x ==0:
        soma = soma+i

        print(f'{i} é multiplo de {x} e sua soma com o resultado anterior é {soma}')
