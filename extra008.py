#Calculadora de Juros Compostos
#Solicite ao usuário o principal, a taxa de juros anual e o número de anos, e imprima o valor do investimento após esse número de anos

def escolha(tempoEdite):
    escolhertempo = input(f'Favor informar se você quer o período como A=Ano'
          f'\n A = Ano'
          f'\n M = Mês'
          f'\n D = Dia: ').upper()
    if escolhertempo == 'A':
        periodo='Ano(s)'
        tempoEdite=tempoEdite
    elif escolhertempo =='M':
        periodo='Mês(es)'
        tempoEdite=tempoEdite/12
    else:
        periodo = 'Dia(s)'
        tempoEdite=tempoEdite/360
    return periodo, tempoEdite

def juroscomposto(Capital,jurosAno,tempoEdite, periodo):
    rendimento = Capital*((1+(jurosAno/100))**tempoEdite)
    print (f'baseando-se nesses moldes de juros {jurosAno}% ao ano no período de {tempo} {periodo} informado teremos um montante de R${rendimento:.2f} em cima dos R${Capital:.2f} investido')

Capital=float(input('Favor informar o Montante investido: '))
jurosAno=float(input('Favor informar os juros composto ao ano(%): '))
tempo=int(input('Favor informar o tempo que você quer que seja calculado o Juros: '))
periodo, tempoEdite = escolha(tempo)
juroscomposto(Capital,jurosAno,tempoEdite, periodo)
