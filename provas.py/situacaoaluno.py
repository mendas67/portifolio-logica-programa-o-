import os
os.system('cls')

print('digite sua nota')
nota = float(input())
if (nota >= 7 ):
    print('Você foi aprovado')

elif (nota > 5):
    print('Recuperação')
else:
    print('Você foi reprovado')
