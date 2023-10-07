#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário

#s(t) = So + Vo *  t + (((a*(t**2)/2)

PosicaoInicial = float(input('Favor informar a posiçao inical: '))
velocidadeInicial = float(input('Favor informar a velocidade inicial: '))
aceleracao = float(input('Favor informar a aceleração: '))
Tempo= float(input('Favor informar o Tempo que você quer saber a posição:'))

formula = PosicaoInicial+velocidadeInicial*Tempo+(aceleracao*(Tempo**2)/2)

print(f'A posição do objeto no tempo {Tempo:2f} é de {formula:2f} (m)')
