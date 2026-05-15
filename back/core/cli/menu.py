import os
# Importando as funções dos seus módulos (certifique-se que os nomes dos arquivos estão corretos)
from back.core.repositories import genero as genero
from back.core.repositories import subgenero as subgenero
from back.core.repositories import ideia as ideia
from back.core.repositories import personagem as personagem
from back.core.repositories import papel_personagem as papel
from back.core.repositories import ideia_personagem as elenco
from back.core.repositories import ideia_cenario as cenario_vinculo
from back.core.repositories import log_ideia as logs


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_principal():
    while True:
        # limpar_tela() # Opcional: limpa o terminal a cada ação
        print("\n" + "=" * 40)
        print("      🌟 INSPIRE SCRIPT - SISTEMA 🌟")
        print("=" * 40)
        print("1. 📝 GERENCIAR IDEIAS (Histórias)")
        print("2. 👤 GERENCIAR PERSONAGENS")
        print("3. 🏷️  GERENCIAR GÊNEROS / SUBGÊNEROS")
        print("4. 🎭 GERENCIAR PAPÉIS (Protagonista...)")
        print("5. 📜 VER HISTÓRICO DE ALTERAÇÕES (LOGS)")
        print("0. ❌ SAIR")
        print("=" * 40)

        opcao = input("Escolha uma categoria: ")

        if opcao == "1":
            menu_ideias()
        elif opcao == "2":
            menu_personagens()
        elif opcao == "3":
            menu_generos()
        elif opcao == "4":
            menu_papeis()
        elif opcao == "5":
            logs.listar_historico_alteracoes()
        elif opcao == "0":
            print("Até logo, autora! ✍️")
            break
        else:
            print("Opção inválida!")


def menu_ideias():
    while True:
        print("\n--- 📝 MENU DE IDEIAS ---")
        print("1. Criar Nova Ideia")
        print("2. Listar Todas (Resumo)")
        print("3. Ver Detalhes (História + Gênero)")
        print("4. Ver Elenco da História")
        print("5. Vincular Subgênero à Ideia")
        print("6. Atualizar Ideia")
        print("7. Deletar Ideia")
        print("0. Voltar")

        op = input("Ação: ")

        if op == "1":
            titulo = input("Título: ")
            sub = input("Subtítulo (opcional): ")
            desc = input("Descrição: ")
            genero.listar_generos()
            id_gen = input("ID do Gênero Principal: ")
            ideia.inserir_ideia(titulo, id_gen, sub, desc)
        elif op == "2":
            ideia.listar_ideias()
        elif op == "3":
            id_id = input("ID da Ideia: ")
            ideia.buscar_ideia_detalhada(id_id)
        elif op == "4":
            id_id = input("ID da Ideia para ver o elenco: ")
            elenco.listar_elenco_da_ideia(id_id)
        elif op == "5":
            id_id = input("ID da Ideia: ")
            subgenero.listar_subgeneros()
            id_sub = input("ID do Subgênero: ")
            subgenero.vincular_subgenero_ideia(id_id, id_sub)
        elif op == "6":  # Atualizar
            ideia.listar_ideias()  # Mostra as ideias para você ver o ID
            id_edit = input("ID da ideia que deseja editar: ")
            novo_tit = input("Novo Título: ")
            novo_sub = input("Novo Subtítulo: ")
            nova_desc = input("Nova Descrição: ")
            genero.listar_generos()
            novo_gen = input("ID do Novo Gênero (Deixe vazio para não alterar): ")
            if novo_gen == "":
                pass
            ideia.atualizar_ideia(id_edit, novo_tit, novo_gen, novo_sub, nova_desc)
        elif op == "7":  # Deletar
            ideia.listar_ideias()
            id_del = input("ID da ideia que deseja DELETAR: ")
            confirmar = input(f"Tem certeza que deseja apagar a ideia {id_del}? (s/n): ")
            if confirmar.lower() == 's':
                ideia.deletar_ideia(id_del)
        elif op == "0":
            break


def menu_personagens():
    while True:
        print("\n--- 👤 MENU DE PERSONAGENS ---")
        print("1. Cadastrar Personagem")
        print("2. Listar Todos")
        print("3. Vincular Personagem a uma Ideia")
        print("4. Remover Personagem de uma Ideia (Desvincular)")
        print("0. Voltar")

        op = input("Ação: ")
        if op == "1":
            nome = input("Nome: ")
            desc = input("Descrição/Ficha: ")
            personagem.inserir_personagem(nome, desc)
        elif op == "2":
            personagem.listar_personagens()
        elif op == "3":
            personagem.listar_personagens()
            id_p = input("ID Personagem: ")
            ideia.listar_ideias()
            id_i = input("ID Ideia: ")
            papel.listar_papeis()
            id_pap = input("ID Papel (Protagonista, etc): ")
            elenco.vincular_personagem_ideia(id_i, id_p, id_pap)
        elif op == "4":
            ideia.listar_ideias()
            id_i = input("ID da Ideia: ")
            elenco.listar_elenco_da_ideia(id_i)  # Mostra quem está na história
            id_p = input("ID do Personagem que deseja remover desta história: ")
            elenco.remover_personagem_da_ideia(id_i, id_p)
        elif op == "0":
            break


def menu_generos():
    while True:
        print("\n--- 🏷️ MENU DE GÊNEROS ---")
        print("1. Cadastrar Gênero Principal")
        print("2. Listar Gêneros")
        print("3. Cadastrar Subgênero")
        print("4. Listar Subgêneros")
        print("0. Voltar")

        op = input("Ação: ")
        if op == "1":
            nome = input("Nome do Gênero (ex: Terror): ")
            genero.inserir_genero(nome)
        elif op == "2":
            genero.listar_generos()
        elif op == "3":
            genero.listar_generos()
            id_pai = input("ID do Gênero Pai: ")
            nome_sub = input("Nome do Subgênero (ex: Slasher): ")
            subgenero.inserir_subgenero(nome_sub, id_pai)
        elif op == "4":
            subgenero.listar_subgeneros()
        elif op == "0":
            break


def menu_papeis():
    while True:
        print("\n--- 🎭 MENU DE PAPÉIS ---")
        print("1. Cadastrar Novo Papel (ex: Antagonista)")
        print("2. Listar Papéis Existentes")
        print("0. Voltar")

        op = input("Ação: ")
        if op == "1":
            nome = input("Nome do Papel: ")
            papel.inserir_papel(nome)
        elif op == "2":
            papel.listar_papeis()
        elif op == "0":
            break


if __name__ == "__main__":
    menu_principal()