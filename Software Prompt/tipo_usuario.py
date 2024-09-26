import mysql.connector
from mysql.connector import Error

class TipoUsuarioDB:
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

    def inserir_tipo_usuario(self, tipo):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "INSERT INTO tipoUsuario (tipo) VALUES (%s)"
                cursor.execute(sql_query, (tipo,))
                self.connection.commit()
                print(f"Tipo de usuário '{tipo}' inserido com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")
        else:
            print("Não há conexão ativa com o banco de dados.")

    def listar_tipos_usuario(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM tipoUsuario")
                tipos = cursor.fetchall()
                if tipos:
                    print("Lista de Tipos de Usuários:")
                    for tipo in tipos:
                        print(f"ID: {tipo[0]}, Tipo: {tipo[1]}")
                else:
                    print("Nenhum tipo de usuário cadastrado.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")
        else:
            print("Não há conexão ativa com o banco de dados.")