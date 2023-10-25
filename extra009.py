#Simulador de Caixa Eletrônico
#Simule um caixa eletrônico. Primeiro pergunte ao usuário qual valor ele quer retirar, depois dê o dinheiro com o menor número possível de notas.

ValorSolicitado = int(input('Informe o valor que será retirado:'))
Notas = [200, 100, 50, 20, 5, 2]

def menorquantidade():
    sobra = ValorSolicitado
    for i in Notas:
        if sobra >= i:
            quantidade = sobra//i
            sobra=sobra%i
            print(f'Quantidade de notas {i} é: {quantidade}')

menorquantidade()



