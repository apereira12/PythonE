#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

def doador(idade,peso,horasSono):

    if idade >= 16 or idade <=69:

        if peso >=50:

            if horasSono>=8:
                print('Você pode doar Sangue')
            else:
                print('Você não pode doar porque dormiu pouco')
        else:
            print('Você não tem peso ideal')

    else:
        print('Você não pode doar sangue')

idade = int(input('Favor informar a idade:'))
peso = float(input('Qual seu peso?:'))
horasSono = int(input('Favor informar suas horas sono:'))


doador(idade,peso,horasSono)
