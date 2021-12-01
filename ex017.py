###Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

catetoOposto = float(input('Escreva o cateto Oposto: '))
catetoAdjacente = float(input('Escreva o cateto adjacente: '))

hip = catetoOposto / catetoAdjacente

print('Num Triangulo Retangulo o Cateto Oposto = {} Dividido pelo Cateto Adjacente {} e igual a Hipotenuso {:.2f}'.format(catetoOposto, catetoAdjacente, hip))

