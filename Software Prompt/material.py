import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class MaterialDB:
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

    def inserir_material(self, nome, descricao, categoria_id):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "INSERT INTO material (nome, descricao, categoria_idcategoria) VALUES (%s, %s, %s)"
                cursor.execute(sql_query, (nome, descricao, categoria_id))
                self.connection.commit()
                print(f"Material '{nome}' inserido com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_materiais(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    SELECT m.idmaterial, m.nome, m.descricao, c.categoria AS categoria
                    FROM material m
                    INNER JOIN categoria c ON m.categoria_idcategoria = c.idcategoria
                """)
                materiais = cursor.fetchall()
                if materiais:
                    print("\n=== Materiais Cadastrados ===")
                    headers = ["ID", "Nome", "Descrição", "Categoria"]
                    print(tabulate(materiais, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhum material cadastrado.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_material(self, id_material, novo_nome, nova_descricao, categoria_id):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "UPDATE material SET nome = %s, descricao = %s, categoria_idcategoria = %s WHERE idmaterial = %s"
                cursor.execute(sql_query, (novo_nome, nova_descricao, categoria_id, id_material))
                self.connection.commit()
                print(f"Material ID {id_material} atualizado.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_material(self, id_material):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM material WHERE idmaterial = %s"
                cursor.execute(sql_query, (id_material,))
                self.connection.commit()
                print(f"Material ID {id_material} excluído com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

## Funções de interface para o menu de materiais
def cadastrar_material(db_material):
    nome = input("Digite o nome do material: ")
    descricao = input("Digite a descrição do material: ")
    categoria_id = input("Digite o ID da categoria do material: ")
    db_material.inserir_material(nome, descricao, categoria_id)

def editar_material(db_material):
    id_material = input("Digite o ID do material que deseja editar: ")
    novo_nome = input("Digite o novo nome do material: ")
    nova_descricao = input("Digite a nova descrição do material: ")
    categoria_id = input("Digite o novo ID da categoria do material: ")
    db_material.atualizar_material(id_material, novo_nome, nova_descricao, categoria_id)

def excluir_material(db_material):
    id_material = input("Digite o ID do material que deseja excluir: ")
    db_material.excluir_material(id_material)
