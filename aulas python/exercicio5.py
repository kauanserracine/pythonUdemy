"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input("Digite um número:")
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print("Você não digitou um número inteiro")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Digite que horas são em números inteiros:")

try:
    hora = int(entrada)

    if hora >= 0 and hora <=11:
        print("Bom dia, flor do dia!")
    elif hora >= 12 and hora <=17:
        print("Boa tarde, covarde!!")
    elif hora >=18 and hora <=23:
        print("Boa noite, vai dormir, amanhã vai tankar o bostil!!")
    else:
        print("Não digitou um horário válido")
except:
    print("Por favor, digite algo válido")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome:")
tamanho_nome = len(nome)

if tamanho_nome > 2:
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    if tamanho_nome >= 5 and tamanho_nome <=6:
        print("Seu nome é normal")
    if tamanho_nome >=6 and tamanho_nome <=19:
        print("Seu nome é grande")
    if tamanho_nome >20:
        print("Ai zuo")        
else:
    print("Por favor, digite algo válido")