#Escreva um script que leia 3 números e mostre o maior e o menor deles

import math

nums = []
for i in range(3):
    print("{}° número: ".format(i + 1))
    n = int(input())
    nums.append(n)

nums.sort()
print("Maior: {}".format(nums[2]))
print("Menor: {}".format(nums[0]))