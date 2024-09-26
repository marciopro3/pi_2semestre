import mysql.connector
from mysql.connector import Error

class UsuarioDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Conexão com o banco de dados estabelecida.")
        except Error as e:
            print(f"Erro ao conectar no banco de dados: {e}")
            self.connection = None

    def desconectar(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")

    def inserir_usuario(self, nome, email, telefone, data_cadastro, tipo_usuario_id):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                INSERT INTO usuario                                                      
                (nome, email, telefone, dataCadastro, tipoUsuario_idtipoUsuario) 
                VALUES (%s, %s, %s, %s, %s)                                                
                """
                valores = (nome, email, telefone, data_cadastro, tipo_usuario_id)
                cursor.execute(sql_query, valores)
                self.connection.commit()
                print(f"Usuário '{nome}' inserido com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")
        else:
            print("Não há conexão ativa com o banco de dados.")

    ## Função para listar todos os usuários cadastrados
    def listar_usuarios(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                SELECT u.idusuario, u.nome, u.email, u.telefone, u.dataCadastro, tu.tipo
                FROM usuario u
                JOIN tipoUsuario tu ON u.tipoUsuario_idtipoUsuario = tu.idtipoUsuario;
                """
                cursor.execute(sql_query)
                usuarios = cursor.fetchall()

                if usuarios:
                    print("\n=== Usuários Cadastrados ===")
                    for usuario in usuarios:
                        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Telefone: {usuario[3]}, Data de Cadastro: {usuario[4]}, Tipo: {usuario[5]}")
                else:
                    print("Nenhum usuário cadastrado.")
            except Error as e:
                print(f"Erro ao consultar dados: {e}")
        else:
            print("Não há conexão ativa com o banco de dados.")

## Função para cadastrar um novo usuário
def cadastrar_usuario(db_usuario):
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    data_cadastro = input("Digite a data de cadastro (AAAA-MM-DD): ")
    tipo_usuario_id = input("Digite o ID do tipo de usuário: ")
    
    db_usuario.inserir_usuario(nome, email, telefone, data_cadastro, tipo_usuario_id)