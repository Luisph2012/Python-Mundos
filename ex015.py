# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


km_carro = float(input('Escreva a Quantidade de KM rodados: '))
diasalugados_carro = int(input('Escreva a Quantidade de Dias rodados: '))

totalpreco_carro = float((km_carro * 0.15) + (diasalugados_carro * 60))

print('O Preco do carro e R$ {2:.2f} por {1} Dias e {0:.0f} Quilometros rodados'.format(km_carro, diasalugados_carro, totalpreco_carro))

