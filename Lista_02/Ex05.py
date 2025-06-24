# Faça um programa que valide as informações:
# Nome: maior que 3 caracteres
# Idade: entre 0 e 150
# Salário: maior que 0
# Sexo: 'm' ou 'f'
# Estado civil: 's', 'c', 'v', 'd'

print("Informe o nome: ")
nome = input()
while len(nome) <= 3:
    print("O nome deve conter mais de 3 caracteres")
    print("Informe o nome: ")
    nome = input()

print("Informe a idade: ")
idade = int(input())
while idade < 0 or idade > 150:
    print("A idade deve estar entre 0 e 150")
    print("Informe a idade: ")
    idade = int(input())

print("Informe o salário: ")
salario = float(input())
while salario <= 0:
    print("O salário deve ser maior que 0")
    print("Informe o salário: ")
    salario = float(input())

print("Informe o sexo: ")
sexo = input()
while sexo not in ["m", "f"]:
    print("O sexo deve ser 'm' ou 'f'")
    print("Informe o sexo: ")
    sexo = input()

print("Informe o estado civil: ")
civil = input()
while civil not in ["s", "c", "v", "d"]:
    print("O estado civil deve ser 's', 'c', 'v' ou 'd'")
    print("Informe o estado civil: ")
    civil = input()