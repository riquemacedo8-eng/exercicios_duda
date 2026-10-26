# # ================ QUESTÃO 01 ==================== 

potencia = int(input("Qual a potencia de switch (w)?"))
horas = int(input("Qual horas por dia"))
tarifa = float(input("Qual o valor da tarifa (kmh)"))

consumo = (potencia * horas * 30) / 1000
custo = consumo * tarifa 

print(f"Consumo: {consumo:.2f} kwh")
print(f"Custo :  R$ {custo:.2f}")


# ================ QUESTÃO 02 ====================

def classificar_latencia(ms):
    if ms < 0: 
        return "Inválido"
    elif ms < 100:
        return "Excelente"
    elif ms < 300:
        return "Adequado"
    elif ms < 1000: 
        return "Degradado"
    else:
        return "Critico"

# ================ QUESTÃO 03 ======================

total = 0
quantidade = 0
valor = 0 
while valor != -1:
    valor = float(input("Digite um valor (-1 para encerrar): "))
    if valor == 1:
        break
    total = total + valor
    quantidade = quantidade + 1

print("Média dos valores:", total / quantidade)


