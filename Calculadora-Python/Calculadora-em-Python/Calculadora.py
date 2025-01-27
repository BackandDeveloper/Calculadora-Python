#

numero1 = int(input)(("Número 1:"))
operacao = int(input)("Operação:")
numero2 = int(input)("Número 2:")

match operacao: 
    case 1:
        print(f'{numero1 + numero2}')
    case 2: 
        print(f'{numero1 - numero2}')
    case 3:
        print(f'{numero1 * numero2}')
    case 4:
        print(f'{numero1 / numero2}')
    case _:
        print ("Operação Inválida!")

    