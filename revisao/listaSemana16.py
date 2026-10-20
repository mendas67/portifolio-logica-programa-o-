import os
os.system ('cls')

import os
os.system('cls')

temperaturas = [22, 25, 21, 24, 26, 23, 22]

i = 0
while i < len(temperaturas):
    print(temperaturas[i])
    i += 1

soma = 0
i = 0
while i < len(temperaturas):
    soma = soma + temperaturas[i]
    i += 1
media = soma / len(temperaturas)

procurada = 24
encontrou = False
i = 0
while i < len(temperaturas):
    if temperaturas[i] == procurada:
        encontrou = True
    i += 1

menor = maior = temperaturas[0]

for i in temperaturas:
    if (i > maior):
        maior = i
    if (i < menor):
        menor = i

print(f'Maior número é: {maior}')
print(f'Menor número é: {menor}')