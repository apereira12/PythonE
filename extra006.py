#Simulador de Dados
#Simule o lançamento de dois dados e imprima a soma dos resultados.
import random


def dados(dado1,dado2):
    soma=dado1+dado2
    return f'o dado 1 caiu o número {dado1} e o dado 2 caiu o número {dado2} e a soma dos dois é {soma}'


for i in range(10):
    dado1 = random.randrange(1,6)
    dado2 = random.randrange(1,6)
    print(f'o número da jogada é {i+1} e {dados(dado1, dado2)}')