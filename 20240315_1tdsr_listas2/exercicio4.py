#A jornada de trabalho diária de um trabalhador é de 8 horas. Caso o trabalhador tenha
#trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. O valor
#da hora-extra é o valor que ele recebe por hora acrescido de 50%. Supondo que ele trabalhe
#apenas nos dias úteis, escreva um algoritmo que recebe:
#a) o total de dias úteis de um mês
#b) o total de horas trabalhadas pelo trabalhador
#c) quanto o trabalhador recebe por hora
#Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário nal do
#trabalhador.

dias_uteis = float(input("Qual o total de dias úteis do mes? "))
total_horas_trabalhadas = float(input("Qual o total de horas trabalhadas? "))
recebe_hora = float(input("Quanto o trabalhador recebe por hora? "))

horas_mensais = dias_uteis * 8
horas_extras = total_horas_trabalhadas - horas_mensais
valor_horas_extras =  (horas_extras * recebe_hora) * 0.5 + (horas_extras * recebe_hora)
salario = recebe_hora * horas_mensais
salario_mais_horas_extras = salario + valor_horas_extras

if horas_extras <= 0 :
    print("Voce tem um salário de:",salario_mais_horas_extras)
else :
    print("O seu salário é: R$", salario, "\nCom um total de:",horas_extras, "hora(s) extras, com o valor de: R$", valor_horas_extras, "\nCom um total de: R$", salario_mais_horas_extras)