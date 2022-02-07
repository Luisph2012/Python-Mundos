#Escreva um programa que leia dois números inteiros e compare-os.
#mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais



num1 = int(input('Escreva um número: '))
num2 = int(input('Escreva mais um número: '))

if num1 > num2:
    print('O Número {} é maior que o {}'.format(num1,num2))
elif num2 > num1:
    print('O Número {} é Menor que o {}'.format(num1,num2))
else:
    print('Os dois números são iguais!')

