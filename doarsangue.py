import os
os.system('cls || clear')

idade = int(input('Digite sua idade: \n'))
peso = float(input('Digite seu peso: \n'))

if (idade >= 18) and (idade <= 69) and (peso > 50):
    print('Voce pode doar sangue')
else:
    print('Voce esta inelegivel para doar sangue')