#A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha
#trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor
#da hora-extra é o valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalhe
#apenas nos dias úteis, escreva um algoritmo que recebe:
#a) o total de dias úteis de um mês
#b) o total de horas trabalhadas pelo trabalhador
#c) quanto o trabalhador recebe por hora
#Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário nal do
#trabalhador.

dias_uteis = int(input("Qual o total de dias úteis do mes? "))
total_horas_trabalhadas = int(input("Qual o total de horas trabalhadas? "))
recebe_hora = int(input("Quanto o trabalhador recebe por hora? "))

horas_mensais = dias_uteis * 8
horas_extras = total_horas_trabalhadas - horas_mensais
salario = recebe_hora * horas_mensais
valor_horas_extras =  horas_extras * 0,5

if horas_extras == 0 :
    print("Voce tem um salário de:",salario)
else :
    print("O seu salário é:", salario, "\nCom um total de:", valor_horas_extras, "horas extras.")