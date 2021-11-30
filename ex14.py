###Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.


temperatura_c = float(input('Informe a Temperatura em Celsius: '))

x = temperatura_c * 9

valorF = (x + 160)/5


print('O Valor de {} em C e igual {:.2f}F (Fahrenheit)'.format(temperatura_c, valorF))