import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class CidadeDB:
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

    def inserir_cidade(self, nome, estado_idestado):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "INSERT INTO cidade (nome, estado_idestado) VALUES (%s, %s)"
                cursor.execute(sql_query, (nome, estado_idestado))
                self.connection.commit()
                print(f"Cidade '{nome}' inserida com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_cidades(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT idcidade, nome, estado_idestado FROM cidade")
                cidades = cursor.fetchall()
                if cidades:
                    print("\n=== Cidades Cadastradas ===")
                    headers = ["ID Cidade", "Nome", "ID Estado"]
                    print(tabulate(cidades, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhuma cidade cadastrada.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_cidade(self, idcidade, estado_idestado, novo_nome):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "UPDATE cidade SET nome = %s WHERE idcidade = %s AND estado_idestado = %s"
                cursor.execute(sql_query, (novo_nome, idcidade, estado_idestado))
                self.connection.commit()
                print(f"Cidade ID {idcidade} atualizada.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_cidade(self, idcidade, estado_idestado):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM cidade WHERE idcidade = %s AND estado_idestado = %s"
                cursor.execute(sql_query, (idcidade, estado_idestado))
                self.connection.commit()
                print(f"Cidade ID {idcidade} excluída com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

# Funções de interface para o menu de cidades
def cadastrar_cidade(db_cidade):
    nome = input("Digite o nome da cidade: ")
    estado_idestado = input("Digite o ID do estado (2 letras): ")
    db_cidade.inserir_cidade(nome, estado_idestado)

def editar_cidade(db_cidade):
    idcidade = int(input("Digite o ID da cidade que deseja editar: "))
    estado_idestado = input("Digite o ID do estado da cidade: ")
    novo_nome = input("Digite o novo nome da cidade: ")
    db_cidade.atualizar_cidade(idcidade, estado_idestado, novo_nome)

def excluir_cidade(db_cidade):
    idcidade = int(input("Digite o ID da cidade que deseja excluir: "))
    estado_idestado = input("Digite o ID do estado da cidade: ")
    db_cidade.excluir_cidade(idcidade, estado_idestado)