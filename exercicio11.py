salario_antes = float(input("Qual era o seu salário? "))
salario_atual = float(input("Qual é o seu salário atual? "))

valor_aumento = (salario_atual - salario_antes)
porcentagem_aumento = 100 - (salario_antes * 100) / salario_atual 

print(f"O valor de aumento do seu salário foi de: R$ {round(valor_aumento, 2)}, em pocentagem é de {round(porcentagem_aumento, 2)} % a mais.")
