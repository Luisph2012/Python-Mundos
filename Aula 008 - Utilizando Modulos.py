#IMPORTs

#import (import tudo)
#from x import x/2 (de x vai importar so um pedaco)

#{import math

#ceil (arredonda pra cima) floor (arredonda pra baixo)
#trunc (elimida da virgula pra frente)
#pow potencia
#sqrt raiz quadrada
#factorial Fatorial}

#
#
#

#so quero raiz quadrada e o arredondamento
#from math import sqrt, ceil


#import math
from math import sqrt, ceil

numero = int (input('Digite um numero: '))
#raiz = math.sqrt(numero)

raiz = sqrt(numero)
#print(raiz)
#print(math.ceil(raiz))


print(ceil(raiz))
print((raiz))

import random

num = random.random()
print (num)

num1 = random.randint(1,312)
print (num1)

import emoji

print (emoji.emojize("Ola :earth_americas:", use_aliases=True))
print (emoji.emojize("Ola :sunglasses:", use_aliases=True))



