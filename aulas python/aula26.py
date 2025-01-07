"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
b0 = '*'
b1 = '***'
b2 = '*****'
b3 = '*******'
b4 = '*********'

print(f'{b0}')
print(f'{b0: >10}')
print(f'{b0: <10}')
print(f'{b0: ^10}')
print(f'{b1: ^10}')
print(f'{b2: ^10}')
print(f'{b3: ^10}')
print(f'{b4: ^10}')



print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{b0!r}')
