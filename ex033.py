#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Escreva um numero: '))
print('-=-' * 20)

b = int(input('Escreva um numero: '))
print('-=-' * 20)

c = int(input('Escreva um numero: '))
print('-=-' * 20)

menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c


maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print('O Menor número é o {} e o Maior número é o {}'.format(menor, maior))