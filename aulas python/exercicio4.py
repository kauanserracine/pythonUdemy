#exercico 4

nome = input('Seu nome:') 
idade = input("Sua idade:") 

if nome and idade :
    print(f'Seu nome é:{nome}') 
    print(f'Sua idade é: {idade}')

    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    
    print(f'Seu nome invetido é: {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é:{nome[0]}') 
    print(f'A última letra do seu nome é:{nome[-1]}') 

else:
    print('Desculpe você deixou campos vazios.')