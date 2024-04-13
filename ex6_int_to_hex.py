num = int(input("Informe número inteiro: "))
resultado = ""


while num != 0: 

    resto = num % 16
    num = num // 16

    if resto == 10:
        resultado = str("A") + resultado
    elif resto == 11:
        resultado = str("B") + resultado
    elif resto == 12:
        resultado = str("C") + resultado
    elif resto == 13:
        resultado= str("D") + resultado
    elif resto == 14:
        resultado= str("E") + resultado
    elif resto == 15:
        resultado = str("F") + resultado
    else:
        resultado = str(resto) + resultado

    


print(f"Hexadecimal: {resultado}")
   

