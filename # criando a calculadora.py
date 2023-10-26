# criando a calculadora 
print('CALCULADORA PYTHON')
print('\n soma = 1','\n subtração = 2', '\n multiplicação = 3', '\n divisão = 4')
soma = lambda arg1,arg2: arg1+arg2
subt = lambda arg1,arg2: arg1-arg2
mult = lambda arg1,arg2: arg1*arg2
divs = lambda arg1,arg2: arg1/arg2

operação = int(input('Favor escolha um número da Operação:'))
if operação > 4: print('Opção inválida')
elif operação == 1: print(soma(int(input('escolha um numero:')),int(input('escolha outro número:'))))
elif operação == 2: print(subt(int(input('escolha um numero:')),int(input('escolha outro número:'))))
elif operação == 3: print(mult(int(input('escolha um numero:')),int(input('escolha outro número:'))))
elif operação == 4: print(divs(int(input('escolha um numero:')),int(input('escolha outro número:'))))
