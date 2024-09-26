from menu import menu
from tipo_usuario import TipoUsuarioDB
from usuario import UsuarioDB

if __name__ == "__main__":
    ##Instancia o banco de dados (criar a instancia com esse mesmo nome e senha no computador de vocês seus puto).
    db_tipo_usuario = TipoUsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_usuario = UsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    
    ##Conectar no banco
    db_tipo_usuario.conectar()
    db_usuario.conectar()

    ##Chama o menu
    menu(db_tipo_usuario, db_usuario)

    ##Desconecta do banco
    db_tipo_usuario.desconectar()
    db_usuario.desconectar()