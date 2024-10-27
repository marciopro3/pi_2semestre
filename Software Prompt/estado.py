import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class EstadoDB:
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
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")

    def inserir_estado(self, id_estado, nome):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "INSERT INTO estado (idestado, nome) VALUES (%s, %s)"
                cursor.execute(sql_query, (id_estado, nome))
                self.connection.commit()
                print(f"Estado '{nome}' inserido com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_estados(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT idestado, nome FROM estado")
                estados = cursor.fetchall()
                if estados:
                    print("\n=== Estados Cadastrados ===")
                    headers = ["ID Estado", "Nome"]
                    print(tabulate(estados, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhum estado cadastrado.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_estado(self, id_estado, novo_nome):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "UPDATE estado SET nome = %s WHERE idestado = %s"
                cursor.execute(sql_query, (novo_nome, id_estado))
                self.connection.commit()
                print(f"Estado ID {id_estado} atualizado.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_estado(self, id_estado):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM estado WHERE idestado = %s"
                cursor.execute(sql_query, (id_estado,))
                self.connection.commit()
                print(f"Estado ID {id_estado} excluído com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

## Funções de interface para o menu de estados
def cadastrar_estado(db_estado):
    id_estado = input("Digite o ID do estado (2 letras): ")
    nome = input("Digite o nome do estado: ")
    db_estado.inserir_estado(id_estado, nome)

def editar_estado(db_estado):
    id_estado = input("Digite o ID do estado que deseja editar: ")
    novo_nome = input("Digite o novo nome do estado: ")
    db_estado.atualizar_estado(id_estado, novo_nome)

def excluir_estado(db_estado):
    id_estado = input("Digite o ID do estado que deseja excluir: ")
    db_estado.excluir_estado(id_estado)
