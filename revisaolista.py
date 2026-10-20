import os
os.system('cls')

import os
os.system('cls')

# cor1 = 'Azul'
# cor2 = 'Amarelo'...
cores = ['Azul', 'Amarelo', 'Branco', 'Cinza', 'Preto']

print(cores) #mostrar a lista por completo
print(cores[0]) #mostrar apenas o 1º item

for cor in cores:
    print(cor) #mostra todos os elementos de dentro da lista
modificavel = [1, 2, 3, 4, 5]
print(modificavel) # [1, 2, 3, 4, 5]
modificavel[0] = 0 #1º posição vira 0
print(modificavel) # [0, 2, 3, 4, 5]

tupla = (1, 2, 3, 4, 5) 
print(tupla) # (1, 2, 3, 4, 5) 
# tupla[0] = 0 
print(tupla) # erro, pois não pode ser alterado

string = 'PYTHON'
print(string[0]) #P