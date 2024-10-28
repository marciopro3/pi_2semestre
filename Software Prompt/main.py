from time import sleep   
from menu import menu   
from tipo_usuario import TipoUsuarioDB   
from usuario import UsuarioDB   
from categoria import CategoriaDB   
from material import MaterialDB    
from estado import EstadoDB        
from cidade import CidadeDB        
from coletor import ColetorDB      
from agendamento import AgendamentoDB, cadastrar_agendamento, editar_agendamento, excluir_agendamento  
from deposito import DepositoDB  
from entrada import EntradaDB  
from saida import SaidaDB  

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
    sleep(4)   # Aguarda 2 segundos para instanciar o banco, conectar no banco e chamar o menu.

if __name__ == "__main__":
    mostrar_animacao_menu()  

    # Instancia o banco de dados
    db_tipo_usuario = TipoUsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_usuario = UsuarioDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_categoria = CategoriaDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")
    db_material = MaterialDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  
    db_estado = EstadoDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  
    db_cidade = CidadeDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  
    db_coletor = ColetorDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  
    db_agendamento = AgendamentoDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  
    db_deposito = DepositoDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  
    db_entrada = EntradaDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  
    db_saida = SaidaDB(host="localhost", database="SBOReciclaSV", user="root", password="Admin123*")  

    # Conecta no banco
    db_tipo_usuario.conectar()
    db_usuario.conectar()
    db_categoria.conectar()
    db_material.conectar()  
    db_estado.conectar()  
    db_cidade.conectar()  
    db_coletor.conectar()  
    db_agendamento.conectar()  
    db_deposito.conectar()  
    db_entrada.conectar()  
    db_saida.conectar()  

    # Chama o menu principal
    menu(db_tipo_usuario, db_usuario, db_categoria, db_material, db_estado, db_cidade, db_coletor, db_agendamento, db_deposito, db_entrada, db_saida)

    # Desconecta do banco
    db_tipo_usuario.desconectar()
    db_usuario.desconectar()
    db_categoria.desconectar()
    db_material.desconectar()  
    db_estado.desconectar()  
    db_cidade.desconectar()  
    db_coletor.desconectar()  
    db_agendamento.desconectar()  
    db_deposito.desconectar()  
    db_entrada.desconectar()  
    db_saida.desconectar() 