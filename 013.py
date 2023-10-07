'''Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
Em que posição ela aparece na última vez'''

frase = input('Escreva sua frase:').lower()

QtdA= print(frase.count('a'))

primeiroA= frase.find('a')
ultimoA= frase.find('a',-1)

print(f'A frase tem{QtdA} "A"'
      f'\n Na frase "{frase}" o 1º A está em {primeiroA} lugar'
      f'\n Na frase "{frase}" o Último está em {ultimoA+1}')

