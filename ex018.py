###Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians

num = float(input('Digite um Angulo: '))

seno = sin(radians(num))
cos = cos(radians(num))
tg = tan(radians(num))

print('Seno: {:.2f}\nCosseno: {:.3f}\nTangente: {:.3f}\n'.format(seno, cos, tg))
