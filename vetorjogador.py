import os
os.system('cls')

pontuacao = [80, 100, 60, 120]

soma = 0
maior = pontuacao[0]
menor = pontuacao[0]

for i in range(4):
    soma = soma + pontuacao[i]

    if (pontuacao[i] > maior):
        maior = pontuacao[i]
    
    if(pontuacao[i] < menor):
        menor = pontuacao[i]


print(f'O maior número é {maior}')
print(f'O menor número é {menor}')