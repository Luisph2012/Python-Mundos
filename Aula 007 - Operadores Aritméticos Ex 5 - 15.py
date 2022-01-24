#   ==========Operadores=============
#   + | Adição
#   - | Subtração
#   * | Multiplicação
#   / | Divisão
#   **| Potência
#   //| Divisão Inteira
#   % | Resto da Divisão
#####################################
#   pow(x,y) = Potência de outra forma   like
print(pow(5, 2))
#   Raizes = (Raiz Quadrada = x ** 1/2) (Raiz Cubica = x ** 1/3)
print(5 ** 1 / 2)
print(5 ** 1 / 3)
#   =================================
#   Testar se é igual ( == )
print(int(5 + 2))
print(int(5 - 2))
print(int(5 * 2))
print(int(5 * 2))
print(int(5 ** 2))
print(int(5 // 2))
print(int(5 % 2))

# Ordem de Precedência
# 1 =   ()
# 2 =   **
# 3 =   (*) (/) (//) (%)
# 4 =   (+) (-)


print('oi' + 'Olá')
print('Olá ' * 20)


#=======Perguntar e Printar o nome
nome = input("What's Your name: ")
print('Pleasure to meet you {}'.format(nome))


#===========com 20 espaços
print('Pleasure to meet you {:20}'.format(nome))



#===========com 20 espaços ALINHAMENTOS

#Esquerda
print('Pleasure to meet you {:<20}'.format(nome))
#Direita
print('Pleasure to meet you {:>20}'.format(nome))
#Centro
print('Pleasure to meet you {:^20}'.format(nome))

#===========Alinhamentos escolhendo oq vai ser nos espacoes

print('Pleasure to meet you {:=^20}'.format(nome))

print('Pleasure to meet you {:.^20}'.format(nome))

#Especificar
print('Pleasure to meet you {:=^20}'.format(nome))

print(str('Pleasure to meet you {:=^20}'.format(nome)))
print(int(2+2))
print(float(pow(9.56,3)))

print('A Resposta Limitando os Decimais: {:.2f}'.format(float((pow(9.56 ,3)))))

s = 4186.46

print('Esse Texto de Teste As \n vezes pode {} Dois Tres {} Four \n Five {} Olha {}'.format(s, s, s, s), end='>>>')
print('Esse Texto de Teste As vezes pode {} Dois Tres {}'.format(s, s))

