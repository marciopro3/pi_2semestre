from tipo_usuario import TipoUsuarioDB

# Função para exibir o menu
def menu(db):
    while True:
        print("\n=== Menu de Opções ===")
        print("1. Cadastrar tipo de usuário")
        print("2. Mostrar tipos de usuário")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tipo = input("Digite o tipo de usuário que deseja cadastrar: ")
            db.inserir_tipo_usuario(tipo)
        elif opcao == "2":
            db.listar_tipos_usuario()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")
