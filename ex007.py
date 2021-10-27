###Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média###

nome_aluno = (str(input('Escreva o nome do Aluno: ')))
nota1 = (float(input('Escreva a PRIMEIRA nota: ')))
nota2 = (float(input('Escreva a SEGUNDA nota: ')))

media = (nota2 + nota1)/2

print('O Aluno {}, com a primeira nota: {}, e a segunda nota: {}, a media é {:.2f}.'.format(nome_aluno,nota1,nota2,media))
