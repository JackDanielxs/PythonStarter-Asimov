# Faça um programa para uma loja de tintas. O usuário informa a área (m**2) que deseja pintar e o script deve calcular quantas latas de tinta a pessoa deve comprar e o valor.
# Considere que cada litro de tinta pinta 3m**2 e que cada lata contém 18L e custa R$80

import math

print("Informe a área que deseja pintar: ")
area = float(input())

litrosNecessarios = area / 3
latasNecessarias = math.ceil(litrosNecessarios / 18) # Arredonda para cima
preco = latasNecessarias * 80

print("{} Lata(s) -> R${:.2f}".format(latasNecessarias, preco))