from time import sleep  # Importando sleep para a animação
from menu import menu
from tipo_usuario import TipoUsuarioDB
from usuario import UsuarioDB
from categoria import CategoriaDB  # Importando a classe CategoriaDB

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
    sleep(4)  # Delay para damain.pyr um efeito de animação

if __name__ == "__main__":
    mostrar_animacao_menu()  # Chama a animação no início

    # Instancia o banco de dados
    db_tipo_usuario = TipoUsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_usuario = UsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_categoria = CategoriaDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  # Nova instância

    # Conectar no banco
    db_tipo_usuario.conectar()
    db_usuario.conectar()
    db_categoria.conectar()  # Conectando a categoria

    # Chama o menu
    menu(db_tipo_usuario, db_usuario, db_categoria)  # Passando db_categoria para o menu

    # Desconecta do banco
    db_tipo_usuario.desconectar()
    db_usuario.desconectar()
    db_categoria.desconectar()  # Desconectando a categoria