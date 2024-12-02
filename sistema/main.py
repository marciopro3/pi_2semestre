from menus.menu import Menu
from database_conexao.bancodedados import BancoDeDados

#NOME - pedro
#data - 25/11/2024

# Instancia da classe banco de dados (banco) recebendo os dados para realizar a conexão

if __name__ == "__main__":
    banco = BancoDeDados(host="192.168.107.128", user="marcio", password="Admin123*", database="SBOReciclaSV")

    banco.conectar()

    # Criando uma instancia da classe 'Menu' e passando o banco
    menu = Menu(banco)

    # Chamando o menu principal
    opcao = menu.exibir_menu_principal()

    banco.desconectar()
