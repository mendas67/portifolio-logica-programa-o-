import os
os.system('cls || clear')

idade=int(input('Digite sua idade \n'))

if(idade <=12) or (idade >=60):
    print('você tem direto a desconto')
else:
    print('Você não tem direito a desconto')