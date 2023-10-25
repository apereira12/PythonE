#Calculadora de Juros Compostos
#Solicite ao usuário o principal, a taxa de juros anual e o número de anos, e imprima o valor do investimento após esse número de anos

def escolha():
    periodo = input(f'Favor informar o período como A=Ano, M=Mês, D=Dia: ').upper()
    tempo = int(input('Favor informar o tempo que você quer que seja calculado o Juros: '))

    if periodo == 'A':
        periodo='Ano(s)'
        tempoEdite=tempo
    elif periodo =='M':
        periodo='Mês(es)'
        tempoEdite=tempo/12
    elif periodo == 'D':
        periodo = 'Dia(s)'
        tempoEdite=tempo/360
    else:
        print("Entrada inválida. Por favor, escolha entre A, M ou D.")
        return None, None, None

    return periodo, tempoEdite, tempo

def juroscomposto(Capital,jurosAno,tempoEdite, periodo, tempo):
    if tempoEdite == 0:
        print("O tempo de investimento não pode ser 0.")
        return
    rendimento = Capital*((1+(jurosAno/100))**tempoEdite)
    print (f'baseando-se nesses moldes de juros {jurosAno}% ao ano no período de {tempo} {periodo} informado teremos um montante de R${rendimento:.2f} em cima dos R${Capital:.2f} investido')

Capital=float(input('Favor informar o Montante investido: '))
jurosAno=float(input('Favor informar os juros composto ao ano(%): '))
periodo, tempoEdite, tempo = escolha()
if periodo and tempoEdite:
    juroscomposto(Capital,jurosAno,tempoEdite, periodo, tempo)
