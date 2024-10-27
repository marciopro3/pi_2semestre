from usuario import cadastrar_usuario
from categoria import CategoriaDB
from material import MaterialDB
from estado import EstadoDB  # Importando a classe EstadoDB
from cidade import CidadeDB, cadastrar_cidade, editar_cidade, excluir_cidade  # Importando a classe CidadeDB
from coletor import ColetorDB, cadastrar_coletor, editar_coletor, excluir_coletor  # Importando funções do coletor

def menu(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor):
    while True:
        print("\n=== Menu de Opções ===")
        print("1. Inserir")
        print("2. Atualizar")
        print("3. Excluir")
        print("4. Mostrar")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sub_menu_inserir(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor)
        elif opcao == "2":
            sub_menu_atualizar(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor)
        elif opcao == "3":
            sub_menu_excluir(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor)
        elif opcao == "4":
            sub_menu_mostrar(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_inserir(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor):
    while True:
        print("\n=== Submenu: Inserir ===")
        print("1. Cadastrar tipo de usuário")
        print("2. Cadastrar usuário")
        print("3. Cadastrar categoria")
        print("4. Cadastrar material")
        print("5. Cadastrar estado")
        print("6. Cadastrar cidade")  # Opção de cadastrar cidade
        print("7. Cadastrar coletor")  # Nova opção para cadastrar coletor
        print("8. Voltar ao menu anterior")
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
            nome = input("Digite o nome do material: ")
            descricao = input("Digite a descrição do material: ")
            categoria_id = input("Digite o ID da categoria do material: ")
            db_material.inserir_material(nome, descricao, categoria_id)
        elif opcao == "5":
            id_estado = input("Digite o ID do estado (2 letras): ")
            nome_estado = input("Digite o nome do estado: ")
            db_estado.inserir_estado(id_estado, nome_estado)
        elif opcao == "6":
            cadastrar_cidade(db_cidade)  # Chama a função para cadastrar cidade
        elif opcao == "7":
            cadastrar_coletor(db_coletor)  # Chama a função para cadastrar coletor
        elif opcao == "8":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_atualizar(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor):
    while True:
        print("\n=== Submenu: Atualizar ===")
        print("1. Editar tipo de usuário")
        print("2. Editar usuário")
        print("3. Editar categoria")
        print("4. Editar material")
        print("5. Editar estado")
        print("6. Editar cidade")  # Opção de editar cidade
        print("7. Editar coletor")  # Nova opção para editar coletor
        print("8. Voltar ao menu anterior")
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
            tipo_usuario_id = input("Digite o novo tipo de usuário (ID): ")
            db_usuario.atualizar_usuario(id_usuario, novo_nome, novo_email, novo_telefone, tipo_usuario_id)
        elif opcao == "3":
            id_categoria = input("Digite o ID da categoria: ")
            nova_categoria = input("Digite a nova categoria: ")
            db_categoria.atualizar_categoria(id_categoria, nova_categoria)
        elif opcao == "4":
            id_material = input("Digite o ID do material: ")
            novo_nome = input("Digite o novo nome do material: ")
            nova_descricao = input("Digite a nova descrição do material: ")
            categoria_id = input("Digite o novo ID da categoria: ")
            db_material.atualizar_material(id_material, novo_nome, nova_descricao, categoria_id)
        elif opcao == "5":
            id_estado = input("Digite o ID do estado: ")
            novo_nome_estado = input("Digite o novo nome do estado: ")
            db_estado.atualizar_estado(id_estado, novo_nome_estado)
        elif opcao == "6":
            editar_cidade(db_cidade)  # Chama a função para editar cidade
        elif opcao == "7":
            editar_coletor(db_coletor)  # Chama a função para editar coletor
        elif opcao == "8":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_excluir(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor):
    while True:
        print("\n=== Submenu: Excluir ===")
        print("1. Excluir tipo de usuário")
        print("2. Excluir usuário")
        print("3. Excluir categoria")
        print("4. Excluir material")
        print("5. Excluir estado")
        print("6. Excluir cidade")  # Opção de excluir cidade
        print("7. Excluir coletor")  # Nova opção para excluir coletor
        print("8. Voltar ao menu anterior")
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
            id_material = input("Digite o ID do material: ")
            db_material.excluir_material(id_material)
        elif opcao == "5":
            id_estado = input("Digite o ID do estado: ")
            db_estado.excluir_estado(id_estado)
        elif opcao == "6":
            excluir_cidade(db_cidade)  # Chama a função para excluir cidade
        elif opcao == "7":
            excluir_coletor(db_coletor)  # Chama a função para excluir coletor
        elif opcao == "8":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_mostrar(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor):
    while True:
        print("\n=== Submenu: Mostrar ===")
        print("1. Mostrar tipos de usuário")
        print("2. Mostrar usuários")
        print("3. Mostrar categorias")
        print("4. Mostrar materiais")
        print("5. Mostrar estados")
        print("6. Mostrar cidades")  # Opção de mostrar cidades
        print("7. Mostrar coletores")  # Nova opção para mostrar coletores
        print("8. Voltar ao menu anterior")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            db_tipo_usuario.listar_tipos_usuario()
        elif opcao == "2":
            db_usuario.listar_usuarios()
        elif opcao == "3":
            db_categoria.listar_categorias()
        elif opcao == "4":
            db_material.listar_materiais()
        elif opcao == "5":
            db_estado.listar_estados()
        elif opcao == "6":
            db_cidade.listar_cidades()  # Mostrando cidades
        elif opcao == "7":
            db_coletor.listar_coletores()  # Mostrando coletores
        elif opcao == "8":
            break
        else:
            print("Opção inválida, tente novamente.")
