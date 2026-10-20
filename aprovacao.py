import os
os.system('cls || clear')

print("Digite a 1º nota")
nota1 = float(input())
print("Digite a 2º nota")
nota2 = float(input())
print("Digite a 3º nota")
nota3 = float(input())
print("Digite a frequência")
frequencia = float(input())
 
media = (nota1 + nota2 + nota3)/3

if (frequencia < 75):
    print("Você foi reprovado direto")
else:
    if (media >= 7):
        print('Você foi aprovado (a) por frequencia e média. sua média foi: ', media)
    elif (media >= 4) and (media <= 6.9):
     print('Você foi aprovado(a) por frequência, mas ficou de recuperação por média. Sua média foi:',media)

