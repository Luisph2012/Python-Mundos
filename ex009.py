###Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada###

num = (int(input('Escreva um número: ')))

a0 = num * 1
a1 = num * 2
a2 = num * 3
a3 = num * 4
a4 = num * 5
a5 = num * 6
a6 = num * 7
a7 = num * 8
a8 = num * 9
a9 = num * 10

print('Tabuada do número {}:'.format(num))
print('{} x 1: {}\n{} x 2: {}\n{} x 3: {}'.format(num, a0, num, a1, num, a2))
print('{} x 4: {}\n{} x 5: {}\n{} x 6: {}\n{} x 7: {}'.format(num, a3, num, a4, num, a5, num, a6))
print('{} x 8: {}\n{} x 9: {}\n{} x 10: {}'.format(num, a7, num, a8, num, a9))
