import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class DepositoDB:
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

    def inserir_deposito(self, nome, endereco, cep, cidade_idcidade, telefone, capacidadeMaxima, dataCadastro, horaAbertura, horaFechamento):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                    INSERT INTO deposito (nome, endereco, cep, cidade_idcidade, telefone, capacidadeMaxima, dataCadastro, horaAbertura, horaFechamento)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql_query, (nome, endereco, cep, cidade_idcidade, telefone, capacidadeMaxima, dataCadastro, horaAbertura, horaFechamento))
                self.connection.commit()
                print(f"Depósito '{nome}' inserido com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_depositos(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    SELECT 
                        deposito.iddeposito, 
                        deposito.nome, 
                        deposito.endereco, 
                        deposito.cep, 
                        deposito.telefone, 
                        deposito.capacidadeMaxima, 
                        deposito.dataCadastro, 
                        deposito.horaAbertura, 
                        deposito.horaFechamento, 
                        cidade.nome AS nome_cidade 
                    FROM 
                        deposito 
                    INNER JOIN 
                        cidade ON deposito.cidade_idcidade = cidade.idcidade
                """)
                depositos = cursor.fetchall()
                if depositos:
                    print("\n=== Depósitos Cadastrados ===")
                    headers = ["ID Depósito", "Nome", "Endereço", "CEP", "Telefone", "Capacidade Máxima", "Data Cadastro", "Hora Abertura", "Hora Fechamento", "Nome Cidade"]
                    print(tabulate(depositos, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhum depósito cadastrado.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_deposito(self, iddeposito, cidade_idcidade, novo_nome, novo_endereco, novo_cep, novo_telefone, nova_capacidadeMaxima, nova_dataCadastro, nova_horaAbertura, nova_horaFechamento):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                UPDATE deposito 
                SET nome = %s, endereco = %s, cep = %s, telefone = %s, capacidadeMaxima = %s, dataCadastro = %s, horaAbertura = %s, horaFechamento = %s 
                WHERE iddeposito = %s AND cidade_idcidade = %s
                """
                cursor.execute(sql_query, (novo_nome, novo_endereco, novo_cep, novo_telefone, nova_capacidadeMaxima, nova_dataCadastro, nova_horaAbertura, nova_horaFechamento, iddeposito, cidade_idcidade))
                self.connection.commit()
                print(f"Depósito ID {iddeposito} atualizado.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_deposito(self, iddeposito, cidade_idcidade):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM deposito WHERE iddeposito = %s AND cidade_idcidade = %s"
                cursor.execute(sql_query, (iddeposito, cidade_idcidade))
                self.connection.commit()
                print(f"Depósito ID {iddeposito} excluído com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

# Funções de interface para o menu de depósitos
def cadastrar_deposito(db_deposito):
    nome = input("Digite o nome do depósito: ")
    endereco = input("Digite o endereço do depósito: ")
    cep = input("Digite o CEP do depósito: ")
    cidade_idcidade = int(input("Digite o ID da cidade do depósito: "))
    telefone = input("Digite o telefone do depósito: ")
    capacidadeMaxima = float(input("Digite a capacidade máxima do depósito: "))
    dataCadastro = input("Digite a data de cadastro (YYYY-MM-DD): ")
    horaAbertura = input("Digite a hora de abertura (HH:MM:SS): ")
    horaFechamento = input("Digite a hora de fechamento (HH:MM:SS): ")
    db_deposito.inserir_deposito(nome, endereco, cep, cidade_idcidade, telefone, capacidadeMaxima, dataCadastro, horaAbertura, horaFechamento)

def editar_deposito(db_deposito):
    iddeposito = int(input("Digite o ID do depósito que deseja editar: "))
    cidade_idcidade = int(input("Digite o ID da cidade do depósito: "))
    novo_nome = input("Digite o novo nome do depósito: ")
    novo_endereco = input("Digite o novo endereço do depósito: ")
    novo_cep = input("Digite o novo CEP do depósito: ")
    novo_telefone = input("Digite o novo telefone do depósito: ")
    nova_capacidadeMaxima = float(input("Digite a nova capacidade máxima do depósito: "))
    nova_dataCadastro = input("Digite a nova data de cadastro (YYYY-MM-DD): ")
    nova_horaAbertura = input("Digite a nova hora de abertura (HH:MM:SS): ")
    nova_horaFechamento = input("Digite a nova hora de fechamento (HH:MM:SS): ")
    db_deposito.atualizar_deposito(iddeposito, cidade_idcidade, novo_nome, novo_endereco, novo_cep, novo_telefone, nova_capacidadeMaxima, nova_dataCadastro, nova_horaAbertura, nova_horaFechamento)

def excluir_deposito(db_deposito):
    iddeposito = int(input("Digite o ID do depósito que deseja excluir: "))
    cidade_idcidade = int(input("Digite o ID da cidade do depósito: "))
    db_deposito.excluir_deposito(iddeposito, cidade_idcidade)
