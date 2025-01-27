#Exemplo simples do uso do Match no Python, para finaliadade de estudos. 

numero = int(input("Digite um número"))
match numero:
    case 1:
       print ("Domingo")
    case 2:
        print ("Segunda-fer=ira")
    case 3:
        print ("Terça-feira")
    case 4:
        print ("Quarta-feira")
    case 5: 
        print ("Quinta-feira")
    case 6:
        print ("Sexta-feira")
    case 7: 
        print ("Sábado")
    case _:
        print ("Valor Inválido")