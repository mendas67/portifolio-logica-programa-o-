import os
os.system('cls || clear')

print('Digite sua idade')
idade = int(input())

if (idade >= 16):
    print('Voce pode votar')
    if (idade >= 18):
        print('voto obrigatorio')
    else:
        print('voto facultativo')
else:
    print('voce ainda não pode votar')
    print('faltam' , 16 - idade , 'anos')