import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class EntradaDB:
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

    def inserir_entrada(self, usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                INSERT INTO entrada (usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade) 
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql_query, (usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade))
                self.connection.commit()
                print(f"Entrada inserida com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_entradas(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                    SELECT 
                        e.identrada, 
                        u.nome AS nome_usuario, 
                        d.nome AS nome_deposito, 
                        m.nome AS nome_material, 
                        e.dataEntrada, 
                        e.quantidade 
                    FROM 
                        entrada e
                    INNER JOIN usuario u ON e.usuario_idusuario = u.idusuario
                    INNER JOIN deposito d ON e.deposito_iddeposito = d.iddeposito
                    INNER JOIN material m ON e.material_idmaterial = m.idmaterial
                """
                cursor.execute(sql_query)
                entradas = cursor.fetchall()
                if entradas:
                    print("\n=== Entradas Cadastradas ===")
                    headers = ["ID Entrada", "Nome do Usuário", "Nome do Depósito", "Nome do Material", "Data Entrada", "Quantidade"]
                    print(tabulate(entradas, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhuma entrada cadastrada.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")


    def atualizar_entrada(self, identrada, usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                UPDATE entrada 
                SET usuario_idusuario = %s, deposito_iddeposito = %s, material_idmaterial = %s, dataEntrada = %s, quantidade = %s 
                WHERE identrada = %s
                """
                cursor.execute(sql_query, (usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade, identrada))
                self.connection.commit()
                print(f"Entrada ID {identrada} atualizada.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_entrada(self, identrada):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM entrada WHERE identrada = %s"
                cursor.execute(sql_query, (identrada,))
                self.connection.commit()
                print(f"Entrada ID {identrada} excluída com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

# Funções de interface para o menu de entradas
def cadastrar_entrada(db_entrada):
    usuario_idusuario = int(input("Digite o ID do usuário: "))
    deposito_iddeposito = int(input("Digite o ID do depósito: "))
    material_idmaterial = int(input("Digite o ID do material: "))
    dataEntrada = input("Digite a data de entrada (YYYY-MM-DD): ")
    quantidade = float(input("Digite a quantidade: "))
    db_entrada.inserir_entrada(usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade)

def listar_entradas(db_entrada):
    db_entrada.listar_entradas()

def editar_entrada(db_entrada):
    identrada = int(input("Digite o ID da entrada que deseja editar: "))
    usuario_idusuario = int(input("Digite o novo ID do usuário: "))
    deposito_iddeposito = int(input("Digite o novo ID do depósito: "))
    material_idmaterial = int(input("Digite o novo ID do material: "))
    dataEntrada = input("Digite a nova data de entrada (YYYY-MM-DD): ")
    quantidade = float(input("Digite a nova quantidade: "))
    db_entrada.atualizar_entrada(identrada, usuario_idusuario, deposito_iddeposito, material_idmaterial, dataEntrada, quantidade)

def excluir_entrada(db_entrada):
    identrada = int(input("Digite o ID da entrada que deseja excluir: "))
    db_entrada.excluir_entrada(identrada)