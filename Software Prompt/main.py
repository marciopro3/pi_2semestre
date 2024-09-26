from menu import menu
from tipo_usuario import TipoUsuarioDB

if __name__ == "__main__":
    # Instancia o banco de dados com os parâmetros de conexão
    db = TipoUsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    
    # Conectar ao banco de dados
    db.conectar()

    # Exibir o menu
    menu(db)

    # Desconectar do banco de dados
    db.desconectar()