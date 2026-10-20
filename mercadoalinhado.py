import os
os.system('cls')

prateleiras = ['prateleira1', 'prateleira2', 'prateleira3', 'prateleira4', 'prateleira5']

produtos = ['produto1', 'produto2', 'produto3', 'produto4', 'produto5']

# print(prateleiras[0], produtos[0])
# print(prateleiras[0], produtos[0])
# print(prateleiras[0], produtos[0])
# print(prateleiras[0], produtos[0])
# print(prateleiras[0], produtos[0])

# for i in range(5):
#     print(prateleiras[i])

# for prateleira in prateleiras:
#     for produto in produtos:
#         print(prateleiras,produtos)


for i in range(5):
    for j in range(4):
        print(prateleiras[i], produtos[j])