import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class SaidaDB:
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

    def inserir_saida(self, deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                INSERT INTO saida (deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade) 
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql_query, (deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade))
                self.connection.commit()
                print("Saída inserida com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_saidas(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                    SELECT 
                        s.idsaida, 
                        d.nome AS nome_deposito, 
                        c.nome AS nome_coletor, 
                        m.nome AS nome_material, 
                        s.dataSaida, 
                        s.quantidade 
                    FROM 
                        saida s
                    INNER JOIN deposito d ON s.deposito_iddeposito = d.iddeposito
                    INNER JOIN coletor c ON s.coletor_idcoletor = c.idcoletor
                    INNER JOIN material m ON s.material_idmaterial = m.idmaterial
                """
                cursor.execute(sql_query)
                saidas = cursor.fetchall()
                if saidas:
                    print("\n=== Saídas Cadastradas ===")
                    headers = ["ID Saída", "Nome do Depósito", "Nome do Coletor", "Nome do Material", "Data Saída", "Quantidade"]
                    print(tabulate(saidas, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhuma saída cadastrada.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_saida(self, idsaida, deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                UPDATE saida 
                SET deposito_iddeposito = %s, coletor_idcoletor = %s, material_idmaterial = %s, dataSaida = %s, quantidade = %s 
                WHERE idsaida = %s
                """
                cursor.execute(sql_query, (deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade, idsaida))
                self.connection.commit()
                print(f"Saída ID {idsaida} atualizada.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_saida(self, idsaida):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM saida WHERE idsaida = %s"
                cursor.execute(sql_query, (idsaida,))
                self.connection.commit()
                print(f"Saída ID {idsaida} excluída com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

# Funções de interface para o menu de saídas
def cadastrar_saida(db_saida):
    deposito_iddeposito = int(input("Digite o ID do depósito: "))
    coletor_idcoletor = int(input("Digite o ID do coletor: "))
    material_idmaterial = int(input("Digite o ID do material: "))
    dataSaida = input("Digite a data de saída (YYYY-MM-DD): ")
    quantidade = float(input("Digite a quantidade: "))
    db_saida.inserir_saida(deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade)

def listar_saidas(db_saida):
    db_saida.listar_saidas()

def editar_saida(db_saida):
    idsaida = int(input("Digite o ID da saída que deseja editar: "))
    deposito_iddeposito = int(input("Digite o novo ID do depósito: "))
    coletor_idcoletor = int(input("Digite o novo ID do coletor: "))
    material_idmaterial = int(input("Digite o novo ID do material: "))
    dataSaida = input("Digite a nova data de saída (YYYY-MM-DD): ")
    quantidade = float(input("Digite a nova quantidade: "))
    db_saida.atualizar_saida(idsaida, deposito_iddeposito, coletor_idcoletor, material_idmaterial, dataSaida, quantidade)

def excluir_saida(db_saida):
    idsaida = int(input("Digite o ID da saída que deseja excluir: "))
    db_saida.excluir_saida(idsaida)