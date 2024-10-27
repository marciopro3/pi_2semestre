from time import sleep   # Biblioteca de animação
from menu import menu   # Importa a classe menu
from tipo_usuario import TipoUsuarioDB   # Importa a classe TipoUsuarioDB
from usuario import UsuarioDB   # Importa a classe UsuarioDB
from categoria import CategoriaDB   # Importa a classe CategoriaDB
from material import MaterialDB    # Importa a classe MaterialDB
from estado import EstadoDB        # Importa a classe EstadoDB
from cidade import CidadeDB        # Importa a classe CidadeDB
from coletor import ColetorDB      # Importa a classe ColetorDB

def mostrar_animacao_menu():
    animacao = r"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |    _______   | || |     _____    | || |    _______   | || |  _________   | || |  _________   | || | ____    ____ | || |      __      | |  
| |   /  ___  |  | || |    |_   _|   | || |   /  ___  |  | || | |  _   _  |  | || | |_   ___  |  | || ||_   \  /   _|| || |     /  \     | |  
| |  |  (__ \_|  | || |      | |     | || |  |  (__ \_|  | || | |_/ | | \_|  | || |   | |_  \_|  | || |  |   \/   |  | || |    / /\ \    | |  
| |   '.___`-.   | || |      | |     | || |   '.___`-.   | || |     | |      | || |   |  _|  _   | || |  | |\  /| |  | || |   / ____ \   | |  
| |  |`\____) |  | || |     _| |_    | || |  |`\____) |  | || |    _| |_     | || |  _| |___/ |  | || | _| |_\/_| |_ | || | _/ /    \ \_ | |  
| |  |_______.'  | || |    |_____|   | || |  |_______.'  | || |   |_____|    | || | |_________|  | || ||_____||_____|| || ||____|  |____|| |  
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |  _______     | || |  _________   | || |     ______   | || |     _____    | || |     ______   | || |   _____      | || |      __      | |  
| | |_   __ \    | || | |_   ___  |  | || |   .' ___  |  | || |    |_   _|   | || |   .' ___  |  | || |  |_   _|     | || |     /  \     | |  
| |   | |__) |   | || |   | |_  \_|  | || |  / .'   \_|  | || |      | |     | || |  / .'   \_|  | || |    | |       | || |    / /\ \    | |  
| |   |  __ /    | || |   |  _|  _   | || |  | |         | || |      | |     | || |  | |         | || |    | |   _   | || |   / ____ \   | |  
| |  _| |  \ \_  | || |  _| |___/ |  | || |  \ `.___.'\  | || |     _| |_    | || |  \ `.___.'\  | || |   _| |__/ |  | || | _/ /    \ \_ | |  
| | |____| |___| | || | |_________|  | || |   `._____.'  | || |    |_____|   | || |   `._____.'  | || |  |________|  | || ||____|  |____|| |  
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   
    """
    print(animacao)
    sleep(4)   # Aguarda 4 segundos para instanciar o banco, conectar no banco e chamar o menu.

if __name__ == "__main__":
    mostrar_animacao_menu()   # Chama a animação

    # Instancia o banco de dados
    db_tipo_usuario = TipoUsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_usuario = UsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_categoria = CategoriaDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_material = MaterialDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  # Instancia o material
    db_estado = EstadoDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  # Instancia o estado
    db_cidade = CidadeDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  # Instancia a cidade
    db_coletor = ColetorDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  # Instancia o coletor

    # Conecta no banco
    db_tipo_usuario.conectar()
    db_usuario.conectar()
    db_categoria.conectar()
    db_material.conectar()  # Conecta o material
    db_estado.conectar()  # Conecta o estado
    db_cidade.conectar()  # Conecta a cidade
    db_coletor.conectar()  # Conecta o coletor

    # Chama o menu principal
    menu(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor)  # Passa o coletor ao menu

    # Desconecta do banco
    db_tipo_usuario.desconectar()
    db_usuario.desconectar()
    db_categoria.desconectar()
    db_material.desconectar()  # Desconecta o material
    db_estado.desconectar()  # Desconecta o estado
    db_cidade.desconectar()  # Desconecta a cidade
    db_coletor.desconectar()  # Desconecta o coletor
