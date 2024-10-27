from usuario import cadastrar_usuario
from categoria import CategoriaDB
from material import MaterialDB
from estado import EstadoDB
from cidade import CidadeDB, cadastrar_cidade, editar_cidade, excluir_cidade
from coletor import ColetorDB, cadastrar_coletor, editar_coletor, excluir_coletor
from agendamento import AgendamentoDB, cadastrar_agendamento, editar_agendamento, excluir_agendamento
from deposito import DepositoDB, cadastrar_deposito, editar_deposito, excluir_deposito
from entrada import EntradaDB, cadastrar_entrada, listar_entradas, editar_entrada, excluir_entrada
from saida import SaidaDB, cadastrar_saida, listar_saidas, editar_saida, excluir_saida  

def menu(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida):
    while True:
        print("\n=== Menu de Opções ===")
        print("1. Inserir")
        print("2. Atualizar")
        print("3. Excluir")
        print("4. Mostrar")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sub_menu_inserir(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida)
        elif opcao == "2":
            sub_menu_atualizar(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida)
        elif opcao == "3":
            sub_menu_excluir(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida)
        elif opcao == "4":
            sub_menu_mostrar(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_inserir(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida):
    while True:
        print("\n=== Submenu: Inserir ===")
        print("1. Cadastrar tipo de usuário")
        print("2. Cadastrar usuário")
        print("3. Cadastrar categoria")
        print("4. Cadastrar material")
        print("5. Cadastrar estado")
        print("6. Cadastrar cidade")
        print("7. Cadastrar coletor")
        print("8. Cadastrar agendamento")
        print("9. Cadastrar depósito")
        print("10. Cadastrar entrada")
        print("11. Cadastrar saída")  
        print("12. Voltar ao menu anterior")
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
            cadastrar_cidade(db_cidade)
        elif opcao == "7":
            cadastrar_coletor(db_coletor)
        elif opcao == "8":
            cadastrar_agendamento(db_agendamento)
        elif opcao == "9":
            cadastrar_deposito(db_deposito)
        elif opcao == "10":
            cadastrar_entrada(db_entrada)
        elif opcao == "11":
            cadastrar_saida(db_saida)  
        elif opcao == "12":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_atualizar(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida):
    while True:
        print("\n=== Submenu: Atualizar ===")
        print("1. Editar tipo de usuário")
        print("2. Editar usuário")
        print("3. Editar categoria")
        print("4. Editar material")
        print("5. Editar estado")
        print("6. Editar cidade")
        print("7. Editar coletor")
        print("8. Editar agendamento")
        print("9. Editar depósito")
        print("10. Editar entrada")
        print("11. Editar saída")  
        print("12. Voltar ao menu anterior")
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
            editar_cidade(db_cidade)
        elif opcao == "7":
            editar_coletor(db_coletor)
        elif opcao == "8":
            editar_agendamento(db_agendamento)
        elif opcao == "9":
            editar_deposito(db_deposito)
        elif opcao == "10":
            editar_entrada(db_entrada)
        elif opcao == "11":
            editar_saida(db_saida)  
        elif opcao == "12":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_excluir(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida):
    while True:
        print("\n=== Submenu: Excluir ===")
        print("1. Excluir tipo de usuário")
        print("2. Excluir usuário")
        print("3. Excluir categoria")
        print("4. Excluir material")
        print("5. Excluir estado")
        print("6. Excluir cidade")
        print("7. Excluir coletor")
        print("8. Excluir agendamento")
        print("9. Excluir depósito")
        print("10. Excluir entrada")
        print("11. Excluir saída")  
        print("12. Voltar ao menu anterior")
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
            excluir_cidade(db_cidade)
        elif opcao == "7":
            excluir_coletor(db_coletor)
        elif opcao == "8":
            excluir_agendamento(db_agendamento)
        elif opcao == "9":
            excluir_deposito(db_deposito)
        elif opcao == "10":
            excluir_entrada(db_entrada)
        elif opcao == "11":
            excluir_saida(db_saida)  
        elif opcao == "12":
            break
        else:
            print("Opção inválida, tente novamente.")

def sub_menu_mostrar(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida):
    while True:
        print("\n=== Submenu: Mostrar ===")
        print("1. Mostrar tipos de usuários")
        print("2. Mostrar usuários")
        print("3. Mostrar categorias")
        print("4. Mostrar materiais")
        print("5. Mostrar estados")
        print("6. Mostrar cidades")
        print("7. Mostrar coletores")
        print("8. Mostrar agendamentos")
        print("9. Mostrar depósitos")
        print("10. Mostrar entradas")
        print("11. Mostrar saídas")  
        print("12. Voltar ao menu anterior")
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
            db_cidade.listar_cidades()  
        elif opcao == "7":
            db_coletor.listar_coletores()  
        elif opcao == "8":
            db_agendamento.listar_agendamentos()  
        elif opcao == "9":
            db_deposito.listar_depositos()  
        elif opcao == "10":
            listar_entradas(db_entrada)  
        elif opcao == "11":
            listar_saidas(db_saida) 
        elif opcao == "12":
            break
        else:
            print("Opção inválida, tente novamente.")