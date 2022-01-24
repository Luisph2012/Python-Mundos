#( faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados)

#numero = str(input('Escreva um número de 0 a 9999: '))

#print('Sepadamente os numeros são: ')
#print(numero[0])
#print(numero[1])
#print(numero[2])
#print(numero[3])

#print('\n\n')

num = int(input('Escreva um número de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))