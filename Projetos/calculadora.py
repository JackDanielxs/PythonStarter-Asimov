# Calculadora - Daniel Marques

import os

operacoes = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponenciação",
    "0": "Sair"
}

while True:
    os.system("")

    i = 0
    for op, name in operacoes.items():
        print(i, ":", name)
        i += 1

    print("")
    print("Escolha a operação:")
    operacao = int(input())
    nomeOperacao = list(operacoes.keys())[operacao]

    if operacao == 5: # Sair do programa
        break

    print("")
    print("Primeiro valor:")
    v1 = float(input())
    print("Segundo valor:")
    v2 = float(input())

    if operacao == 0: # Soma
        result = v1 + v2
    elif operacao == 1: # Subtração
        result = v1 - v2
    elif operacao == 2: # Multiplicação
        result = v1 * v2
    elif operacao == 3: # Divisão
        result = v1 / v2
    elif operacao == 4: # Exponenciação
        result = v1 ** v2

    print("")
    print("{} {} {} = {}".format(v1, nomeOperacao, v2, result))
    print("")
