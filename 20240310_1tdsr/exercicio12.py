rm = int(input("Qual seu RM?"))
soma = 0

dig = rm % 10
soma = soma + dig #acmulador
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

print("A soma vale: ", soma)