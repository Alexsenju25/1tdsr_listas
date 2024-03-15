print("***Iremos calcular a velocidade média e km do seu corredor***")
distancia_em_metros = int(input(("Qual a distancia em metros? ")))
tempo_em_segundos = float(input("Qual o tempo do seu corredor em segundos? "))

velocidade_media_ms = distancia_em_metros / tempo_em_segundos

distancia_km = distancia_em_metros / 1000
tempo_em_horas = tempo_em_segundos / 3600
velocidade_media_km = distancia_km / tempo_em_horas

print("A velocidade média do seu corredor em m/s é de", round(velocidade_media_ms, 2),"e em Km/r é de", round(velocidade_media_km, 2))


