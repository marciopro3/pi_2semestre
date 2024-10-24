import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

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

    def inserir_usuario(self, nome, email, telefone, tipo_usuario_id):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "INSERT INTO usuario (nome, email, telefone, tipoUsuario_idtipoUsuario) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_query, (nome, email, telefone, tipo_usuario_id))
                self.connection.commit()
                print(f"Usuário '{nome}' inserido com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_usuarios(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM usuario")
                usuarios = cursor.fetchall()
                if usuarios:
                    print("\n=== Usuários Cadastrados ===")
                    for usuario in usuarios:
                        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Telefone: {usuario[3]}")
                else:
                    print("Nenhum usuário cadastrado.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_usuario(self, id_usuario, novo_nome, novo_email, novo_telefone):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "UPDATE usuario SET nome = %s, email = %s, telefone = %s WHERE idusuario = %s"
                cursor.execute(sql_query, (novo_nome, novo_email, novo_telefone, id_usuario))
                self.connection.commit()
                print(f"Usuário ID {id_usuario} atualizado.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_usuario(self, id_usuario):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM usuario WHERE idusuario = %s"
                cursor.execute(sql_query, (id_usuario,))
                self.connection.commit()
                print(f"Usuário ID {id_usuario} excluído com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

# Funções de interface para o menu
def cadastrar_usuario(db_usuario):
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    data_cadastro = input("Digite a data de cadastro (AAAA-MM-DD): ")
    tipo_usuario_id = input("Digite o ID do tipo de usuário: ")
    db_usuario.inserir_usuario(nome, email, telefone, data_cadastro, tipo_usuario_id)

def editar_usuario(db_usuario):
    id_usuario = input("Digite o ID do usuário que deseja editar: ")
    nome = input("Digite o novo nome do usuário: ")
    email = input("Digite o novo email do usuário: ")
    telefone = input("Digite o novo telefone do usuário: ")
    tipo_usuario_id = input("Digite o novo ID do tipo de usuário: ")
    db_usuario.editar_usuario(id_usuario, nome, email, telefone, tipo_usuario_id)

def excluir_usuario(db_usuario):
    id_usuario = input("Digite o ID do usuário que deseja excluir: ")
    db_usuario.excluir_usuario(id_usuario)