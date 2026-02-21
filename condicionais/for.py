#permite repetir um codigo enquanto a condição for verdadeira
#for serve pra interar uma sequencia de elementos

lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(f"esse é o resultado:", elemento)

tupla = (1, 2, 3, 4, 5)
for cuzin in tupla:
    print(f"quantidade de pessoas q ja botaram no cuzin de valdemar:", cuzin)

pessoa = {"nome": "Gabriel", "Idade": "18", "naturalidade": "Campina Grande"}
print(f"com dicionario:")
for chave in pessoa.keys():
    print(chave)

#range(): intervalo númerico em formato de lista
# [0, 1, 2, 3, 4, 5]

print(list(range(0, 10)))