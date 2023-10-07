nome = input('Insira seu nome: ')

nome = nome.strip()#Remove espaço

print(f'A primeira letra é {nome[0]}')#Primeira letra


print(f'O tamanho no seu nome é:{len(nome)}')#Tamanho da string

nome = nome.split() #Separar String em lista

print(f'O seu primeiro nome é: {nome[0]}')

print(f'O seu último nome é: {nome[-1]}')

nome = ' '.join(nome)

nome = nome.upper()
print(nome)

nome = nome.lower()
print(nome)

