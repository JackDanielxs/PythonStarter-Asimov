# Escreva um programa que pergunte o nome completo do usuário e cumprimente o mesmo pelo primeiro nome

print("Qual é seu nome completo? ")
nomeCompleto = input()
primeiroNome = nomeCompleto.split(" ")[0]
print("Olá, {}".format(primeiroNome))