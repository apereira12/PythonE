#Verificador de Palíndromos
#- Solicite ao usuário uma palavra e verifique se a palavra é um palíndromo.

palavra = input('Informe a palavra: ').capitalize()
compatibilidade = 0
for i in range(0,len(palavra)):
    if palavra[i] == palavra[i -1]:
        compatibilidade == compatibilidade+1
if compatibilidade == len(palavra):
    print(f'a palavra "{palavra}" é um palíndromo')
else:
    print(f'a palavra "{palavra}" não é um palíndromo')