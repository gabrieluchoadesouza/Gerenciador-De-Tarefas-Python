#criando um dicionario de exemplo chave/valor

pessoa = {"nome": "gabriel", "idade": 30, "cidade": "campina grande"}

print(f"meu dicionário de exemplo:", pessoa)

#acessando valores por chave
print(f"nome:", pessoa["nome"])

#como a gente pode alterar a idade por exemplo

idade = "31"
print(f"idade:", idade)

#exclue chave/valor

del pessoa["cidade"]
print(f"resultado:", pessoa)

#metodos keys() values() items()

chaves = list(pessoa.keys())
print(f"agora a primeira:", chaves[0])

itens = pessoa.items()
print(f"lista de pessoas:", itens)