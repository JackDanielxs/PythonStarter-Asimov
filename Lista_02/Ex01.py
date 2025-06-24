# Faça um programa que leia duas notas parciais de um aluno. Deve-se calcular a média alcançada por aluno e apresentar:
# "Aprovado", se a média for maior ou igual a 7
# "Reprovado", se a média for menor que 7
# "Aprovado com distinção", se a média for 10

print("Insira a primeira nota: ")
nota1 = float(input())
print("Insira a segunda nota: ")
nota2 = float(input())

media = (nota1 + nota2) / 2

if media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")
else:
    print("Aprovado")