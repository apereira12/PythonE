import random


valordisp = random.randrange(0,5000)
Notas = [200, 100, 50, 20, 5, 2]
x = int(input('Favor informar sua escolha:'
                    '\n 1 - Depósito '
                    '\n 2 - Saques'
                    '\n 3 - consultar o saldo'
                    '\n 4 - Sair   '))




def escolha(x, valordisp, Notas):
    while x != 4:
        if x == 1:
            valordep = float(input('Favor informar o valor do depósito:  '))
            novovalor = valordisp+valordep
            print(f'Você tinha R${valordisp:.2f} e com esse valor de R${valordep:.2f} você tem R$ {novovalor:.2f}')
            break

        elif x == 2:
            valorsolicitado = int(input('Informe o valor que será retirado:  '))
            sobra = valorsolicitado
            print(f'Você tinha R${valordisp:.2f}, seu saldo agora é R${valordisp-valorsolicitado:.2f}')
            for i in Notas:
                if sobra >= i:
                    quantidade = sobra // i
                    sobra = sobra % i
                    print(f'Quantidade de notas {i} é: {quantidade}')
            break
        elif x == 3:
            print(f'Você tem R${valordisp} na conta')
            break
        else:
            print('Operação indisponível')
            break




escolha(x, valordisp, Notas)



