#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

print('------Calcule o seu MMC------')

peso = float(input('Qual é o seu peso (em KG): '))
altura = int(input('Qual é a sua Altura (em CM): '))

altura_metro = altura / 100

imc = peso / (altura_metro * altura_metro)

print('O seu IMC atual é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está \033[1;33mABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está no \033[1;32mPESO ATUAL')
elif 25 <= imc < 30:
    print('Você está em \033[1;33mSOBREPESO')
elif 30 <= imc < 40:
    print('Você está na faixa de \033[1;31mOBESIDADE')
else:
    print('Você em na faixa da \033[1;31mOBESIDADE MÓRBIDA')