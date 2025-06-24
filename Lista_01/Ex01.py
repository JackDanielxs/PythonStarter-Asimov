# Utilizando o built-in method input(), crie um programa que receba a altura e o peso de uma pessoa e calcule e imprima na tela o IMC da mesma

print("Informe sua altura: ")
altura = float(input())
print("Informe seu peso: ")
peso = float(input())

imc = peso / (altura ** 2)
print("Seu IMC é: {:.2f}".format(imc))