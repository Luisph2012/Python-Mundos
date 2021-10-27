###Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros###

valorEmKm = (float(input('Escreva um Valor em KM (Quilômetros): ')))

valorEmCm = valorEmKm * 100
valorEmMm = valorEmKm * 1000

print('O valor em KM é {}\nEle em Cm é {}\nEle em Mm é {}'.format(valorEmKm, valorEmCm, valorEmMm))