#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual é a distância da viagem (em KM): '))

if distancia <= 200:
    valor1 = distancia * 0.5
    print('-=-' * 20)
    print('O valor da passagem é de {:.2f} pela viagem com a distância de {:.0f}!'.format(valor1, distancia))
    print('-=-' * 20)
else:
    valor2 = distancia * 0.45
    print('-=-' * 20)
    print('O valor da passagem é de {:.2f} pela viagem com a distância de {:.0f}!'.format(valor2, distancia))
    print('-=-' * 20)

print('Boa Viagem!')


