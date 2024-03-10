valor_produto = float(input("Qual o valor do produto? R$"))
aumento_ou_desconto = input("Será um aumento ou um desconto? (Digite 's' para aumento e 'n' para desconto) ")
desicao = False

if aumento_ou_desconto == "n" :
    desconto = float(input("Qual o percentual do desconto? Digite o valor sem '%'. "))
    valor_desconto = desconto / 100 * valor_produto
    valor_desconto_sobre_produto = valor_produto - valor_desconto 
    print("O valor do desconto é: R$", valor_desconto, " e o novo valor do produto é de: R$",valor_desconto_sobre_produto)
elif aumento_ou_desconto == "s" :
    aumento = float(input("Qual o percentual do aumento? Digite o valor sem '%'. "))
    valor_aumento = aumento / 100 * valor_produto
    valor_aumento_sobre_produto = valor_produto + valor_aumento
    print("O valor do aumento é: R$", valor_aumento, " e o novo valor do produto é de: R$", valor_aumento_sobre_produto)
else :
    print("Valor incorreto, por favor digite novamente.")
        
