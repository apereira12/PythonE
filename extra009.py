#Simulador de Caixa Eletrônico
#Simule um caixa eletrônico. Primeiro pergunte ao usuário qual valor ele quer retirar, depois dê o dinheiro com o menor número possível de notas.

ValorSolicitado = int(input('Informe o valor que será retirado:'))
Notas=[2,5,20,50,100,200]

def menorquantidade():
    for i in Notas:
        divisao=ValorSolicitado/i
        print(f'Nota de {i}: {divisao}')

menorquantidade()



