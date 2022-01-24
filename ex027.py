#(Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.)


nome_completo = str(input('Digite seu nome completo: ').strip())

nome_separado = nome_completo.split()

print('O seu primeiro nome é: {}'.format(nome_separado[0]))
print('O seu Ultimo nome é: {}'.format(nome_separado[len(nome_separado)-1]))



