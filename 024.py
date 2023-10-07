#Escreva um programa que peça ao
# usuário uma senha e verifique se ela está correta (a senha correta é "python123").

def correta():
    if senha == 'python123':
        print('A senha está correta')
    else:
        print('A senha está incorreta')

senha = input('Favor informar a senha: ')

correta()