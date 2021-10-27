###Faça um programa que leia a largura e a altura de uma parede em metros,
###calcule a sua área e a quantidade de tinta necessária para pintá-la,
###sabendo que cada litro de tinta, pinta uma área de 2m^2

altura  = float(input('Qual a Altura (metros): '))
largura = float(input('Qual a Largura (metros): '))

area = altura * largura

litroTinta = area / 2

print('Para área de {}, Você precisará de {} de tinta'.format(area, litroTinta))

