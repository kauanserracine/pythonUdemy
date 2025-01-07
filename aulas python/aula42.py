frase = 'O Pyhton é uma linguagem de progamação, multiparadigma, Pythom foi criado por Guido van Rossum'

i = 0 
qtd_apareceu_mais_vezes = 0
letra_mais_x = ''
while i < len(frase):
    letra_atual = frase [i]
    x_letras = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < x_letras:
        qtd_apareceu_mais_vezes = x_letras
        letra_mais_x = letra_atual

    i += 1
print(
    'A letra que mais apareceu foi '
      f'"{letra_mais_x}"'' que apareceu '
      f'{qtd_apareceu_mais_vezes}x'
)