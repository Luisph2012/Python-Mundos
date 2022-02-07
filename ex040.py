#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO


print('APROVADO OU REPROVADO!!!')
print ('-=-' * 20)
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
print ('-=-' * 20)

media = (nota1 + nota2) / 2

if media >= 7.0:
    print('Parabéns! Você passou com a media {:.2f}'.format(media))
elif media < 5.0:
    print('Você foi Reprovado! Media {:.2f}'.format(media))
else:
    print('Você está de recuperação! media {:.2f}'.format(media))

