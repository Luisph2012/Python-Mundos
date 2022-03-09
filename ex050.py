#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0
for n in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1

if contador == 0:
    print('Você informou NENHUM Numero PAR')
elif contador == 1:
    print('Você informou 1 Número Pá e a soma é {}'.format(soma))
elif contador > 1:
    print('Você informou {} números PARES e a soma foi de {}'.format(contador, soma))

