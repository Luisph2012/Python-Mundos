#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = float(input('Qual é Velocidade do Carro Atualmente: '))

if velocidade_carro >= 80.0:
    print('Você Passou acima da velocidade permitida!')
    print('-=-' * 20)
    velocidade_acima = velocidade_carro - 80.0
    preco_multa = velocidade_acima * 7.0
    print('Pelas Leis de transito você terá que pagar {:.2f} R$ de multa! por ter passado {:.2f} Km acima do permitido.'.format(preco_multa ,velocidade_acima))
    print('-=-' * 20)
print('Boa Viagem! Dirija com Cuidado!')

