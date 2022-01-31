#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Escreva um Numero: '))

if num % 2 == 0:
    print('O número {} é Par!'.format(num))
else:
    print('O número {} é Impar!'.format(num))

print('-=-' * 20)
print('OUTRO JEITO DE FAZER')
print('O número {} é Par!'.format(num) if num % 2 == 0 else 'O número {} é Impar!'.format(num))