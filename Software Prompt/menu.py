from tipo_usuario import TipoUsuarioDB
from usuario import UsuarioDB, cadastrar_usuario

##Função que mostra o menu
def menu(db_tipo_usuario, db_usuario):
    while True:
        print("\n=== Menu de Opções ===")
        print("1. Cadastrar tipo de usuário")
        print("2. Mostrar tipos de usuário")
        print("3. Cadastrar novo usuário")
        print("4. Mostrar usuários cadastrados")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tipo = input("Digite o tipo de usuário que deseja cadastrar: ")
            db_tipo_usuario.inserir_tipo_usuario(tipo)
        elif opcao == "2":
            db_tipo_usuario.listar_tipos_usuario()
        elif opcao == "3":
            cadastrar_usuario(db_usuario)
        elif opcao == "4":
            db_usuario.listar_usuarios()  ##Chama a função que lista os usuários
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")