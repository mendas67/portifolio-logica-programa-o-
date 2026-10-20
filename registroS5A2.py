import os
os.system('cls || clear')

nota1 = float(input('Digite a primeira nota \n'))
nota2 = float(input('Digite a segunda nota \n'))

media = (nota1 + nota2) / 2

if (media >= 6):
    print('Voce foi aprovado')
else:
    print('Voce foi reprovado')