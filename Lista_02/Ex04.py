# Faça um programa capaz de gerar a série de fibonacci até o n-ésimo termo

print("Quantidade de termos: ")
n = int(input())

v0 = 0
v1 = 1
v = 1

print(1)
for i in range(n + 1):
    print("{} ".format(v))
    v0 = v1
    v1 = v
    v = v1 + v0
    