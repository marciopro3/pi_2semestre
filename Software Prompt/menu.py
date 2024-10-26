from usuario import cadastrar_usuario
from categoria import CategoriaDB

def menu(db_tipo_usuario, db_usuario, db_categoria):
    while True:
        print("\n=== Menu de Opções ===")
        print("1. Inserir")
        print("2. Atualizar")
        print("3. Excluir")
        print("4. Mostrar")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sub_menu_inserir(db_tipo_usuario, db_usuario, db_categoria)
        elif opcao == "2":
            sub_menu_atualizar(db_tipo_usuario, db_usuario, db_categoria)
        elif opcao == "3":
            sub_menu_excluir(db_tipo_usuario, db_usuario, db_categoria)
        elif opcao == "4":
            sub_menu_mostrar(db_tipo_usuario, db_usuario, db_categoria)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_inserir(db_tipo_usuario, db_usuario, db_categoria):
    while True:
        print("\n=== Submenu: Inserir ===")
        print("1. Cadastrar tipo de usuário")
        print("2. Cadastrar usuário")
        print("3. Cadastrar categoria")
        print("4. Voltar ao menu anterior")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tipo = input("Digite o tipo de usuário que deseja cadastrar: ")
            db_tipo_usuario.inserir_tipo_usuario(tipo)
        elif opcao == "2":
            cadastrar_usuario(db_usuario)
        elif opcao == "3":
            categoria = input("Digite a categoria que deseja cadastrar: ")
            db_categoria.inserir_categoria(categoria)
        elif opcao == "4":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_atualizar(db_tipo_usuario, db_usuario, db_categoria):
    while True:
        print("\n=== Submenu: Atualizar ===")
        print("1. Editar tipo de usuário")
        print("2. Editar usuário")
        print("3. Editar categoria")
        print("4. Voltar ao menu anterior")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_tipo = input("Digite o ID do tipo de usuário: ")
            novo_tipo = input("Digite o novo tipo de usuário: ")
            db_tipo_usuario.atualizar_tipo_usuario(id_tipo, novo_tipo)
        elif opcao == "2":
            id_usuario = input("Digite o ID do usuário: ")
            novo_nome = input("Digite o novo nome do usuário: ")
            novo_email = input("Digite o novo email do usuário: ")
            novo_telefone = input("Digite o novo telefone do usuário: ")
            db_usuario.atualizar_usuario(id_usuario, novo_nome, novo_email, novo_telefone)
        elif opcao == "3":
            id_categoria = input("Digite o ID da categoria: ")
            nova_categoria = input("Digite a nova categoria: ")
            db_categoria.atualizar_categoria(id_categoria, nova_categoria)
        elif opcao == "4":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_excluir(db_tipo_usuario, db_usuario, db_categoria):
    while True:
        print("\n=== Submenu: Excluir ===")
        print("1. Excluir tipo de usuário")
        print("2. Excluir usuário")
        print("3. Excluir categoria")
        print("4. Voltar ao menu anterior")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_tipo = input("Digite o ID do tipo de usuário: ")
            db_tipo_usuario.excluir_tipo_usuario(id_tipo)
        elif opcao == "2":
            id_usuario = input("Digite o ID do usuário: ")
            db_usuario.excluir_usuario(id_usuario)
        elif opcao == "3":
            id_categoria = input("Digite o ID da categoria: ")
            db_categoria.excluir_categoria(id_categoria)
        elif opcao == "4":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_mostrar(db_tipo_usuario, db_usuario, db_categoria):
    while True:
        print("\n=== Submenu: Mostrar ===")
        print("1. Mostrar tipos de usuário")
        print("2. Mostrar usuários")
        print("3. Mostrar categorias")
        print("4. Voltar ao menu anterior")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            db_tipo_usuario.listar_tipos_usuario()
        elif opcao == "2":
            db_usuario.listar_usuarios()
        elif opcao == "3":
            db_categoria.listar_categorias()
        elif opcao == "4":
            break
        else:
            print("Opção inválida, tente novamente.")