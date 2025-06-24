# Faça um programa que peça um número inteiro e verifique se ele é primo

print("Insira o número: ")
num = int(input())

check = 0
for i in range(2, int(num / 2)):
    if num % i == 0:
        check = 1
        break

if check == 0:
    print("PRIMO")
else:
    print("NÃO PRIMO")