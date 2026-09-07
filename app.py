# Entrada
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas = float(input("Digite o tempo médio de uso diário do aparelho em horas: "))

# Processamento
consumo_mensal = (potencia * horas * 30) / 1000

# Saída
print (f"Seu/sua {aparelho} tem o consumo estimado de {consumo_mensal:.2f} kWh por mês.")