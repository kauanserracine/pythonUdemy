'calculadora com while'

while True:
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    op = input("Digite o operador(+, -, / ou *): ")

    num_val = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        num_val =  True
    except:
        num_val =  None
    if num_val is None:
        print("Um dos números digitados são inválidos.")
        continue

    op_permitidos = '+-/*'
    if op not in op_permitidos:
        print("Você não selecionou um operador permitido.")
        continue

    if len(op) > 1:
        print("Você selecionou mais de um operador.")
        continue

    if op == "+":
        resultado = n1_float + n2_float
        print("O resultado é:", resultado)
    
    elif op == "-":
        resultado = n1_float - n2_float
        print("O resultado é:", resultado)

    elif op == "/":
        resultado = n1_float / n2_float
        (print(f'"O resultado é":, {resultado:.0f}'))

    elif op == "*":
        resultado = n1_float * n2_float
        print("O resultado é:", resultado)

    sair = input("Quer sair?: ").lower().startswith('s')

    if sair is True:
        print("Você saiu, obrigado por utilizar minha calculadora.")
        break
  