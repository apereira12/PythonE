#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima
# se a média é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9)
# ou excelente (9 ou maior).

def notas():
    valor = []
    for i in range(5):
        valor.append(float(input(f'Digite a Nota da prova {i+1}:')))
    media = sum(valor)/5
    print(media)
    if media < 6:
        print('Valor Insuficiente')
    elif media >=6 and media<=7:
        print('Valor Suficiente')
    elif media >7 and media<9:
        print('Bom')
    elif media >=9 and media <11:
        print('Excelente')
    else:
        print('Essa nota não existe')

notas()





