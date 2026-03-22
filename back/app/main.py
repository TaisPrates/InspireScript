from app.crud.genero_crud import listar_generos
from app.crud.ideia_crud import inserir_ideia

from app.crud.genero_crud import (
    inserir_genero,
    listar_generos,
    buscar_genero_por_id,
    atualizar_genero,
    deletar_genero
)

from app.crud.ideia_crud import (
    inserir_ideia,
    listar_ideias,
    buscar_ideia_por_id,
    atualizar_ideia,
    deletar_ideia
)

from app.crud.personagem_crud import (
    inserir_personagem,
    listar_personagens,
    buscar_personagem_por_id,
    atualizar_personagem,
    deletar_personagem
)

from app.crud.cenario_crud import (
    inserir_cenario,
    listar_cenarios,
    buscar_cenario_por_id,
    atualizar_cenario,
    deletar_cenario
)

from app.crud.subgenero_ideia_crud import (
    inserir_subgenero_ideia,
    listar_subgeneros_ideia,
    buscar_subgeneros_por_ideia,
    buscar_ideias_por_subgenero,
    deletar_subgenero_ideia
)

from app.crud.ideia_personagem_crud import (
    inserir_ideia_personagem,
    listar_ideia_personagem,
    buscar_personagens_por_ideia,
    buscar_ideias_por_personagem,
    deletar_ideia_personagem
)

from app.crud.ideia_cenario_crud import (
    inserir_ideia_cenario,
    listar_ideia_cenario,
    buscar_cenarios_por_ideia,
    buscar_ideias_por_cenario,
    deletar_ideia_cenario
)



def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Gênero")
        print("2 - Ideia")
        print("3 - Personagem")
        print("4 - Cenário")
        print("5 - Subgênero da Ideia")
        print("6 - Ideia x Personagem")
        print("7 - Ideia x Cenário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_genero()
        elif opcao == "2":
            menu_ideia()
        elif opcao == "3":
            menu_personagem()
        elif opcao == "4":
            menu_cenario()
        elif opcao == "5":
            menu_subgenero_ideia()
        elif opcao == "6":
            menu_ideia_personagem()
        elif opcao == "7":
            menu_ideia_cenario()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")


def menu_genero():
    while True:
        print("\n===== MENU GÊNERO =====")
        print("1 - Inserir gênero")
        print("2 - Listar gêneros")
        print("3 - Buscar gênero por ID")
        print("4 - Atualizar gênero")
        print("5 - Deletar gênero")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do gênero: ")
            tipo = input("Tipo (principal/subgenero): ")
            id_pai = input("ID do gênero pai (ou deixe vazio): ")

            id_pai = int(id_pai) if id_pai.strip() else None
            inserir_genero(nome, tipo, id_pai)

        elif opcao == "2":
            listar_generos()

        elif opcao == "3":
            id_genero = int(input("ID do gênero: "))
            buscar_genero_por_id(id_genero)

        elif opcao == "4":
            id_genero = int(input("ID do gênero: "))
            nome = input("Novo nome: ")
            tipo = input("Novo tipo (principal/subgenero): ")
            id_pai = input("Novo ID do gênero pai (ou deixe vazio): ")

            id_pai = int(id_pai) if id_pai.strip() else None
            atualizar_genero(id_genero, nome, tipo, id_pai)

        elif opcao == "5":
            id_genero = int(input("ID do gênero: "))
            deletar_genero(id_genero)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_ideia():
    while True:
        print("\n===== MENU IDEIA =====")
        print("1 - Inserir ideia")
        print("2 - Listar ideias")
        print("3 - Buscar ideia por ID")
        print("4 - Atualizar ideia")
        print("5 - Deletar ideia")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            subtitulo = input("Subtítulo: ")

            # 🔽 CORRETO: buscar os gêneros
            generos = listar_generos()

            if not generos:
                print("Nenhum gênero encontrado.")
                continue

            print("\nGêneros disponíveis:")
            for genero in generos:
                print(f"{genero[0]} - {genero[1]}")

            try:
                id_genero_principal = int(input("Escolha o ID do gênero: "))
            except ValueError:
                print("Erro: digite um número.")
                continue

            ids_validos = [genero[0] for genero in generos]

            if id_genero_principal not in ids_validos:
                print("Erro: gênero inválido.")
                continue

            descricao = input("Descrição: ")

            inserir_ideia(titulo, subtitulo, id_genero_principal, descricao)

        elif opcao == "2":
            listar_ideias()

        elif opcao == "3":
            id_ideia = int(input("ID da ideia: "))
            buscar_ideia_por_id(id_ideia)

        elif opcao == "4":
            id_ideia = int(input("ID da ideia: "))
            titulo = input("Novo título: ")
            subtitulo = input("Novo subtítulo: ")
            id_genero_principal = int(input("ID do gênero principal: "))
            descricao = input("Nova descrição: ")

            atualizar_ideia(id_ideia, titulo, subtitulo, id_genero_principal, descricao)

        elif opcao == "5":
            id_ideia = int(input("ID da ideia: "))
            deletar_ideia(id_ideia)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

def menu_personagem():
    while True:
        print("\n===== MENU PERSONAGEM =====")
        print("1 - Inserir personagem")
        print("2 - Listar personagens")
        print("3 - Buscar personagem por ID")
        print("4 - Atualizar personagem")
        print("5 - Deletar personagem")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            papel = input("Papel (principal/coadjuvante): ")

            inserir_personagem(nome, descricao, papel)

        elif opcao == "2":
            listar_personagens()

        elif opcao == "3":
            id_personagem = int(input("ID do personagem: "))
            buscar_personagem_por_id(id_personagem)

        elif opcao == "4":
            id_personagem = int(input("ID do personagem: "))
            nome = input("Novo nome: ")
            descricao = input("Nova descrição: ")
            papel = input("Novo papel (principal/coadjuvante): ")

            atualizar_personagem(id_personagem, nome, descricao, papel)

        elif opcao == "5":
            id_personagem = int(input("ID do personagem: "))
            deletar_personagem(id_personagem)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_cenario():
    while True:
        print("\n===== MENU CENÁRIO =====")
        print("1 - Inserir cenário")
        print("2 - Listar cenários")
        print("3 - Buscar cenário por ID")
        print("4 - Atualizar cenário")
        print("5 - Deletar cenário")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            tipo = input("Tipo (real/fantástico/mistério/outro): ")

            inserir_cenario(nome, descricao, tipo)

        elif opcao == "2":
            listar_cenarios()

        elif opcao == "3":
            id_cenario = int(input("ID do cenário: "))
            buscar_cenario_por_id(id_cenario)

        elif opcao == "4":
            id_cenario = int(input("ID do cenário: "))
            nome = input("Novo nome: ")
            descricao = input("Nova descrição: ")
            tipo = input("Novo tipo (real/fantástico/mistério/outro): ")

            atualizar_cenario(id_cenario, nome, descricao, tipo)

        elif opcao == "5":
            id_cenario = int(input("ID do cenário: "))
            deletar_cenario(id_cenario)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_subgenero_ideia():
    while True:
        print("\n===== MENU SUBGÊNERO DA IDEIA =====")
        print("1 - Vincular subgênero à ideia")
        print("2 - Listar vínculos")
        print("3 - Buscar subgêneros por ideia")
        print("4 - Buscar ideias por subgênero")
        print("5 - Deletar vínculo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_ideia = int(input("ID da ideia: "))
            id_genero = int(input("ID do subgênero: "))
            inserir_subgenero_ideia(id_ideia, id_genero)

        elif opcao == "2":
            listar_subgeneros_ideia()

        elif opcao == "3":
            id_ideia = int(input("ID da ideia: "))
            buscar_subgeneros_por_ideia(id_ideia)

        elif opcao == "4":
            id_genero = int(input("ID do subgênero: "))
            buscar_ideias_por_subgenero(id_genero)

        elif opcao == "5":
            id_ideia = int(input("ID da ideia: "))
            id_genero = int(input("ID do subgênero: "))
            deletar_subgenero_ideia(id_ideia, id_genero)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_ideia_personagem():
    while True:
        print("\n===== MENU IDEIA x PERSONAGEM =====")
        print("1 - Vincular personagem à ideia")
        print("2 - Listar vínculos")
        print("3 - Buscar personagens por ideia")
        print("4 - Buscar ideias por personagem")
        print("5 - Deletar vínculo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_ideia = int(input("ID da ideia: "))
            id_personagem = int(input("ID do personagem: "))
            inserir_ideia_personagem(id_ideia, id_personagem)

        elif opcao == "2":
            listar_ideia_personagem()

        elif opcao == "3":
            id_ideia = int(input("ID da ideia: "))
            buscar_personagens_por_ideia(id_ideia)

        elif opcao == "4":
            id_personagem = int(input("ID do personagem: "))
            buscar_ideias_por_personagem(id_personagem)

        elif opcao == "5":
            id_ideia = int(input("ID da ideia: "))
            id_personagem = int(input("ID do personagem: "))
            deletar_ideia_personagem(id_ideia, id_personagem)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_ideia_cenario():
    while True:
        print("\n===== MENU IDEIA x CENÁRIO =====")
        print("1 - Vincular cenário à ideia")
        print("2 - Listar vínculos")
        print("3 - Buscar cenários por ideia")
        print("4 - Buscar ideias por cenário")
        print("5 - Deletar vínculo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_ideia = int(input("ID da ideia: "))
            id_cenario = int(input("ID do cenário: "))
            inserir_ideia_cenario(id_ideia, id_cenario)

        elif opcao == "2":
            listar_ideia_cenario()

        elif opcao == "3":
            id_ideia = int(input("ID da ideia: "))
            buscar_cenarios_por_ideia(id_ideia)

        elif opcao == "4":
            id_cenario = int(input("ID do cenário: "))
            buscar_ideias_por_cenario(id_cenario)

        elif opcao == "5":
            id_ideia = int(input("ID da ideia: "))
            id_cenario = int(input("ID do cenário: "))
            deletar_ideia_cenario(id_ideia, id_cenario)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()