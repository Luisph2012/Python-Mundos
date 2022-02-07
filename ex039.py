#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date

ano_nasc = int(input('Informe sua data de nascimento: '))

idade = date.today().year - ano_nasc

if idade < 18:
    tempo = 18 - idade
    print('Você não pode se alistar')
    print('Ainda falta {} para você se alistar no ano {}'.format(tempo, ano_nasc + 18))

elif idade > 18:
    tempo = idade - 18
    print('O seu prazo de alistamente passou {} ano era para você se alistar em {} '.format(tempo, ano_nasc + 18))

else:
    print('Você está na Hora de se alistar!!')