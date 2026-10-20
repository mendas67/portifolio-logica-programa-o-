import os
os.system('cls')
acumulador = 5
for contador in range(1,4):
    item = float(input(f'Digite o valor do item {contador} \n'))
    acumulador = acumulador + item

print (acumulador)