# (Faca um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posicao ela aparece a primeira vez
# Em que posicao ela aparece a ultima vez

frase = str(input('Digite uma frase: '))

frase_arrumado = frase.upper().strip()

print('Nessa Frase tem {} Letras "A"'.format(frase_arrumado.count("A")))

print('Aparece pela primeira vez na posição: {}'.format(frase_arrumado.find("A")+1))
print('Aparece pela Ultima vez na posição: {}'.format(frase_arrumado.rfind("A")+1))


