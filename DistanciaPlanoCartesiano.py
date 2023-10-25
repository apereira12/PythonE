# Calculadora de Distância
#Solicite ao usuário as coordenadas de dois pontos (x1, y1, x2, y2) e calcule a distância entre eles.

#formula: ((xb-xa)**2+(yb-ya)**2)**0,5


def formula(x1,x2,y1,y2):
    distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
    print (f'a distância entre os dois pontos é de aproximadamente:{distancia:.2f}')

x1 = float(input('Favor informar o ponto x1:'))
y1 = float(input('Favor informar o ponto y1:'))
x2 = float(input('Favor informar o ponto x2:'))
y2 = float(input('Favor informar o ponto y2:'))

formula(x1,x2,y1,y2)
