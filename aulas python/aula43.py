# senha_salva = '123456'
# senha_digitada = ' '
# rep = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({rep}x): ')

#     rep += 1

# print(rep)
# print('Aquele laço acima pode ter repetições infinitas')

text = 'Python'
novo_texto = ' '
for letra in text:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)