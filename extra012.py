#Conversor de Temperatura
#Solicite ao usuário uma temperatura em graus Celsius e converta-a para graus Fahrenheit (e vice-versa).

UnidadeInicial = input('Favor informar a Unidade de medida'
                '\n C = Celsius'
                '\n F = Fahrenheit: ').lower()
Temperatura = float(input('Informe a Temperatura:'))
Unidade = ''

def conversor(UnidadeInicial, Unidade, Temperatura):
    if UnidadeInicial =="c":
        #formula para conversao F = (C°*9/5)+32
        UnidadeInicial="Cº"
        Unidade = "Fahrenheit"
        Valor= (Temperatura * 9/5 )+ 32.00
    elif UnidadeInicial=="f":
        UnidadeInicial = "Fº"
        Unidade = "Celsius"
        #Formula para conversao C = 5/9 x (F-32)
        Valor =  5/9*(Temperatura-32)

    print(f'A temperatura de {Temperatura}{UnidadeInicial} convertida para {Unidade} é de {Valor}')

conversor(UnidadeInicial, Unidade, Temperatura)