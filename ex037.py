# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um Numero: '))
print('Escolha a Conversão: \n1 - Binário\n2 - Octal\n3 - Hexadecimal')
escolha = int(input('Sua Opção é: '))

if escolha == 1:
    print('Binário: {}'.format(bin(num).replace("0b", "")))
elif escolha == 2:
    print('Octal: {}'.format(oct(num)[2:]))
elif escolha == 3:
    print('Hexadecimal: {}'.format(hex(num)[2:]))
else:
    print('Opção invalida!!!')