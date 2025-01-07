'''PALAVRA SECRETA'''

import os

secreta = 'palmeiras'
letras_acertos = ''
tentativas = 0

while True:

    letra_usuario = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_usuario in secreta:
        letras_acertos += letra_usuario

    palavra_formada = ''
    for letra_secreta in secreta:
        if letra_secreta in letras_acertos:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: ',palavra_formada)

    if palavra_formada == secreta:
        os.system('cls')
        print("Parabéns você acertou a palavra secreta!, que no caso é: ", palavra_formada)
        print("O número de tentativas foi: ",tentativas)
        letras_acertos = ''
        tentativas = 0     
        break