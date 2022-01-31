#Escrever Frases Grande

print("""
Non-autoregressive generation (NAG) has recently attracted great attention due to its fast inference speed. 
However, the generation quality of existing NAG models still lags behind their autoregressive counterparts. 
In this work, we show that BERT can be employed as the backbone of a NAG model to greatly improve performance. 
Additionally, we devise mechanisms to alleviate the two common problems of vanilla NAG models: the inflexibility 
of prefixed output length and the conditional independence of individual token predictions. Lastly, to 
further increase the speed advantage of the proposed model, we propose a new decoding strategy, ratio-first, 
for applications where the output lengths can be approximately estimated beforehand. For a comprehensive evaluation, 
we test the proposed model on three text generation tasks, including text summarization, sentence compression and 
machine translation. Experimental results show that our model significantly outperforms existing non-autoregressive 
baselines and achieves competitive performance with many strong autoregressive models. In addition, we also conduct 
extensive analysis experiments to reveal the effect of each proposed component.""")

#com a formatacao
print('\n\n\n')

#
#   FATIAMENTO
#

#
#   frase[9] (LISTA)
#

#frase = """Non-autoregressive generation (NAG) has recently attracted great attention due to its fast inference speed.
#However, the generation quality of existing NAG models still lags behind their autoregressive counterparts.
#In this work, we show that BERT can be employed as the backbone of a NAG model to greatly improve performance.
#Additionally, we devise mechanisms to alleviate the two common problems of vanilla NAG models: the inflexibility
#of prefixed output length and the conditional independence of individual token predictions. Lastly, to
#further increase the speed advantage of the proposed model, we propose a new decoding strategy, ratio-first,
#for applications where the output lengths can be approximately estimated beforehand. For a comprehensive evaluation,
#we test the proposed model on three text generation tasks, including text summarization, sentence compression and
#machine translation. Experimental results show that our model significantly outperforms existing non-autoregressive
#baselines and achieves competitive performance with many strong autoregressive models. In addition, we also conduct
#extensive analysis experiments to reveal the effect of each proposed component."""
frase = 'prova de python'

print(frase)
print(frase[9])
print(frase[5])
print(frase[4])

#
#   frase[9:13]  pega os caracters do 9 ate o 12
#

print(frase[9:13])
print(frase[9:21])

#
#   Vai do 9 ate o 21 pulando de 2 em 2
#
print(frase[9:21:2])

#
# omitindo o primeiro numero ele comeca do inicio vice versa
#
print(frase[:15])
print(frase[15:])

#
# Testes
#

print(frase[9::3])


#
#   Analise
#

#len = length
contar1 = len(frase)

print('Tem {} Letras'.format(contar1))

#count = contar

LetraParaOCount = 'o'
contar2 = frase.count(LetraParaOCount)
print('Tem {} Letras {}'.format(contar2, LetraParaOCount))

#Contar com Fateamento

contar3 = frase.count(LetraParaOCount,0,13) #da primeira letra ate a letra 12

print('Tem {} Letras {}'.format(contar3, LetraParaOCount))

#find = procurar

#comeca na posicao 11
print(frase.find('deo'))

#Se nao existe o valor e -1
print(frase.find('Android'))

Analise = 'Curso' in frase
Analise2 = 'Luis' in frase
print(Analise)
print(Analise2)

#
#   Transformacao
#
#replace = Substitui de ... para ...

print(frase.replace('Python','Android'))
#deixar maiusculo
print(frase.upper())
#minusculo
print(frase.lower())
#todos minusculo mas a primeira letra em maiusculo
print(frase.capitalize())
#analisa quantas palavras e faz o capitalize em cada palavra
print(frase.title())

frase2 = '   Aprenda Python   '

#remover espacos inuteis
arrumar = frase2.strip()
print(arrumar)
#espacos da direita
arrumar2 = frase2.rstrip()
print(arrumar2)
#espacoes da esquerda
arrumar3 = frase2.lstrip()
print(arrumar3)

#split por padrao ele e feito pelos espacos

separar = frase.split()

print('-'.join(separar))

print(separar)
print(separar[3])
print(separar[2])
print(separar[1])
print(separar[0])
print('--------------'.join(separar))




