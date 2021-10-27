###Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Informe o preço do produto(em real): R$'))

precoDesconto = preco * 0.95

print('O preço atual com desconta é {:.2f}'.format(precoDesconto))