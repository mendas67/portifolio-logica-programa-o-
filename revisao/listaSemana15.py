import os
os.system ('cls')

notas = [7, 8.5, 6, 9, 5.5] #Criando o vetor notas e armazenando 5 valores 

QuantidadeValores = len(notas) # variaVel recebe a quantidade de valoress atraves da função len()
IndicePrimeiroValor = notas.index(7) #Variavel recebe o primeiro valor do prmeiro indice atraves da função index
UltimoIndice = len(notas) -1 # variavel recebe a último valor atraves da subtração de i sobre o número de itens

i = 0 # inicializando o indice i com o valor 0
while i<6: #estrutura while com a condição de parada 
    print(notas[i]) #mostrar cada item da lista, rodada por rodada
    i+= 1 # incrementa i 1 ao valor do index a cada rodada do while

#contar quantas notas existem
print(len(notas))

menor = notas [0]
#identificar a maior nota;
for i in range (5):
    if (notas[i] > maior):
        maior = notas[i]
print(f'O maior número é {maior}')

# somar todas as notas 
soma = 0
for i in notas:
    soma += i
print(soma)

