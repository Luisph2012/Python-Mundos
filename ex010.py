###Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
###Considere
###US$ 1,00 = R$ 3,27


dinheiroAtualReal = float(input('Quanto de Dinheiro (em real) você quer trocar: R$'))

dolar = dinheiroAtualReal / 3.27

print('Você ira comprar US$ {}'.format(dolar))
