import os
os.system('cls || clear')

print("Digite sua idade")
idade = int (input())
if (idade > 0 ) and (idade <=12):
    print("você é uma criança")
if (idade >= 13) and (idade <= 17):
    print("você é um adolescente")
if (idade >= 18) and (idade <= 64):
    print("você é um adulto")
if (idade >= 65):
    print("você é um idoso")