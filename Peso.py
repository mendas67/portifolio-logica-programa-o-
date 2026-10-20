import os
os.system('cls || clear')

peso = float(input("Digite seu peso do pacote \n"))
if(peso >10):
    print("frete expresso")
elif(peso >2):
    print("frete economico")
else:
    tipoFrete = str(input("Digite seu frete \n"))