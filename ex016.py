###Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcao inteira###
###EX: 6.127 print parte inteira = 6
from math import floor

num = float(input('Digite um numero com Virgula: '))
print ('O Valor Inteiro Do numero {} e igual a {}'.format(num, floor(num)))


