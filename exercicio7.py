num = int(input("Escreva um número de 0 a 99: "))
if num > 0 and num <= 99:
    unid =  num % 10
    dezena = num // 10  

    print("A dezena é: ", dezena, "\nA unidade é: ", unid)
else:
    print("Número invalido.")