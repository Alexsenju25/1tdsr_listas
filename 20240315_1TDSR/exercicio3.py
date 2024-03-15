# Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma
# partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a
# palavra EMPATE.

time1 = (input("Digite o nome do 1° time: "))
gols_time1 = int(input("Digite a qtd de gols desse time: "))
time2 = (input("Digite o nome do 2° time: "))
gols_time2 = int(input("Digite a qtd de gols desse time: "))

print("                     Resultado:\n ")
if gols_time1 > gols_time2:
    print(time1, "com um total de", gols_time1, "gols é o vencedor.")
elif gols_time2 > gols_time1:
    print(time2, "com um total de", gols_time2, "gols é o vencedor.")
else:
    print("Houve um empate entre", time1, "e", time2)
