#(Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com ao nome "SANTO"

cidade = str(input('Fale o nome da sua cidade: '))

cidade_sepadado = cidade.split()

cidade_first_name_lower = cidade_sepadado[0].lower()

print('Sua cidade começa com o nome "Santo": {}'.format('santo' in cidade_first_name_lower))

print("\n\n")
#(ERRADO)
if cidade_sepadado[0] == 'Santo':
    print('Sim')
else:
    print('Não')
print('\n')
#(CERTO)
if cidade_first_name_lower == 'santo':
    print('Sim')
else:
    print('Não')
print('\n')


