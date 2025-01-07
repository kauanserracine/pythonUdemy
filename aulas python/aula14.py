a = "AAAA"
b = "BBBB"
c = 1.1
string = 'b={nome_2} a={nome_1} a={nome_1} c={nome_3:.2f}'
formato = string.format(nome_1= a , nome_2= b, nome_3= c)

print(formato)
