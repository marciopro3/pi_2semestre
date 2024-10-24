import mysql.connector
from mysql.connector import Error
from tabulate import tabulate  # Importando a biblioteca tabulate

class CategoriaDB:
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

    def inserir_categoria(self, categoria):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "INSERT INTO categoria (categoria) VALUES (%s)"
                cursor.execute(sql_query, (categoria,))
                self.connection.commit()
                print(f"Categoria '{categoria}' inserida com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_categorias(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM categoria")
                categorias = cursor.fetchall()
                if categorias:
                    # Criando uma tabela com tabulate
                    headers = ["ID", "Categoria"]
                    print("\n=== Categorias Cadastradas ===")
                    print(tabulate(categorias, headers, tablefmt="pretty"))  # Usando tabulate para formatar
                else:
                    print("Nenhuma categoria cadastrada.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_categoria(self, id_categoria, nova_categoria):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "UPDATE categoria SET categoria = %s WHERE idcategoria = %s"
                cursor.execute(sql_query, (nova_categoria, id_categoria))
                self.connection.commit()
                print(f"Categoria ID {id_categoria} atualizada para '{nova_categoria}'.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_categoria(self, id_categoria):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM categoria WHERE idcategoria = %s"
                cursor.execute(sql_query, (id_categoria,))
                self.connection.commit()
                print(f"Categoria ID {id_categoria} excluída com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")
