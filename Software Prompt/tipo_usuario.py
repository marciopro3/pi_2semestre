import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

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

    def listar_tipos_usuario(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM tipoUsuario")
                tipos = cursor.fetchall()
                if tipos:
                    print("\n=== Tipos de Usuários ===")
                    headers = ["ID", "Tipo"]
                    print(tabulate(tipos, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhum tipo de usuário cadastrado.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_tipo_usuario(self, id_tipo, novo_tipo):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "UPDATE tipoUsuario SET tipo = %s WHERE idtipoUsuario = %s"
                cursor.execute(sql_query, (novo_tipo, id_tipo))
                self.connection.commit()
                print(f"Tipo de usuário ID {id_tipo} atualizado para '{novo_tipo}'.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_tipo_usuario(self, id_tipo):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM tipoUsuario WHERE idtipoUsuario = %s"
                cursor.execute(sql_query, (id_tipo,))
                self.connection.commit()
                print(f"Tipo de usuário ID {id_tipo} excluído com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

# Funções de interface para o menu
def cadastrar_tipo_usuario(db_tipo_usuario):
    tipo = input("Digite o tipo de usuário: ")
    db_tipo_usuario.inserir_tipo_usuario(tipo)

def editar_tipo_usuario(db_tipo_usuario):
    id_tipo = input("Digite o ID do tipo de usuário que deseja editar: ")
    novo_tipo = input("Digite o novo tipo de usuário: ")
    db_tipo_usuario.atualizar_tipo_usuario(id_tipo, novo_tipo)

def excluir_tipo_usuario(db_tipo_usuario):
    id_tipo = input("Digite o ID do tipo de usuário que deseja excluir: ")
    db_tipo_usuario.excluir_tipo_usuario(id_tipo)
