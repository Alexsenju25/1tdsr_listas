pagamento_a_vista = float(input("Qual o valor à vista? "))
pagamento_parcela = float(input("Qual o valor da parcela? "))

valor_total_parcela = pagamento_parcela * 10
desconto_a_vista = 100 - (pagamento_a_vista * 100) / valor_total_parcela

print(f"O desconto porcentual é de: {desconto_a_vista}%")