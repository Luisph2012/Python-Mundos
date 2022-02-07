#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

#EX 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Primeira Reta: '))
reta2 = float(input('Segunda Reta: '))
reta3 = float(input('Terceira Reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os Segmentos acima Podem formar Triângulo!')
    if reta1 == reta2 == reta3:
        print('E ele é Equiláteros')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('E ele é Isósceles')
    else:
        print('E ele é Escaleno')
else:
    print('Os Segmentos acima não podem formar Triângulo!')

