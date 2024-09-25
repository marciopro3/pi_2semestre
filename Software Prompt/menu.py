from cadastroUsuario import CadastroUsuario

def menu():
    cadastro = CadastroUsuario()
    
    while True:
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Cadastrar Tipo de Usuário")
        print("4. Listar Tipos de Usuários")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastro.cadastrar_usuario()
        elif opcao == "2":
            cadastro.listar_usuarios()
        elif opcao == "3":
            cadastro.cadastrar_tipo_usuario()
        elif opcao == "4":
            cadastro.listar_tipos_usuario()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
