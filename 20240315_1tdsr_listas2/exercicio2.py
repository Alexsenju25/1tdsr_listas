#Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
#houve um empate.

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite um outro valor: "))

if num1 > num2 :
    print(num1, " é maior que ", num2)
elif num2 > num1 :
    print(num2, " é maior que ", num1)
else :
    print("Houve um empate entre: ", num1, " e ", num2 )
