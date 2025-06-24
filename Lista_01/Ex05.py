# Faça um programa que pergunte quanto o usuário ganha por hora e o número de horas trabalhadas no mês
# Cacule o total do seu salário no referido mês, sabendo que são descontados:
# 11% -> Imposto de renda; 8% -> INSS; 5% -> Sindicato
# Mostre: Salário bruto; Quanto pagou ao INSS; Quanto pagou ao sindicato; Salário líquido

def calcular_porcentagem(valor, porcentagem):
    return valor * (porcentagem / 100)

print("Quanto você ganha por hora? ")
precoHora = float(input())
print("Quantas horas você trabalhou no mês? ")
horas = float(input())

salarioBruto = precoHora * horas
impostoRenda = calcular_porcentagem(salarioBruto, 11)
inss = calcular_porcentagem(salarioBruto, 8)
sindicato = calcular_porcentagem(salarioBruto, 5)
salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print("Salário bruto: {:.2f}".format(salarioBruto))
print("Pago ao INSS: {:.2f}".format(inss))
print("Pago ao sindicato: {:.2f}".format(sindicato))
print("Salário líquido: {:.2f}".format(salarioLiquido))