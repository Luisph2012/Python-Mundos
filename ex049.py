#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num1=int(input('Digite o Número que você quer saber a Tabuada: '))

for i in range(1, 101):
    total = num1*i
    print('{} x {} = {}'.format(num1, i, total))

