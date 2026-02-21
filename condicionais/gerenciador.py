def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"A tarefa {nome_tarefa} foi adicionada com sucesso")
    return

def ver_tarefas(tarefas):
    print(f"\nLista de Tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
      status = "✓" if tarefa ["completada"] else " "
      nome_tarefa = tarefa["nome"]
      print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1 
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} Atualizada para {novo_nome_tarefa}")
    else:
        print(f"Índice de Tarefa Inválido")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado] ["completada"] = True
    print(f"Tarefa {indice_tarefa} Marcada Como Completada")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print(f"Tarefas Completadas Foram Deletadas.")
    return

tarefas = [] 
while True:
    print(f"\nMenu do Gerenciador de Lista de Tarefas:")
    print(f" 1. Adicionar Tarefas:")
    print(f" 2. Ver Tarefas:")
    print(f" 3. Atualizar Tarefas:")
    print(f" 4. Completar Tarefas:")
    print(f" 5. Deletar Taferas Completadas:")
    print(f" 6. Sair")

    escolha = input(f"Digite a sua escolha:")
    if escolha == "1":
        nome_tarefa = input(f"Digite o Nome da Tarefa que Deseja Adicionar:")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input(f"Digite o Numero da Tarefa que Deseja Atualizar:")
        novo_nome = input(f"Digite o Novo Nome da Tarefa:")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input(f" Digite o Número da Tarefa que Deseja Completar:")
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6":
        break
    
print(f"Programa Encerrado o")