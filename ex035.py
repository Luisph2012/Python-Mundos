#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Primeira Reta: '))
reta2 = float(input('Segunda Reta: '))
reta3 = float(input('Terceira Reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os Segmentos acima Podem formar Triângulo!')
else:
    print('Os Segmentos acima não podem formar Triângulo!')

