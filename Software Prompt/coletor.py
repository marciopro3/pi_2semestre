import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class ColetorDB:
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

    def inserir_coletor(self, nome, cnpjCpf, telefone, endereco, cidade_idcidade, dataCadastro):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "INSERT INTO coletor (nome, cnpjCpf, telefone, endereco, cidade_idcidade, dataCadastro) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql_query, (nome, cnpjCpf, telefone, endereco, cidade_idcidade, dataCadastro))
                self.connection.commit()
                print(f"Coletor '{nome}' inserido com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")

    def listar_coletores(self):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    SELECT 
                        coletor.idcoletor, 
                        coletor.nome, 
                        coletor.cnpjCpf, 
                        coletor.telefone, 
                        coletor.endereco, 
                        cidade.nome AS nome_cidade,  -- Seleciona o nome da cidade
                        coletor.dataCadastro 
                    FROM 
                        coletor 
                    INNER JOIN 
                        cidade ON coletor.cidade_idcidade = cidade.idcidade  -- Realiza o JOIN
                """)
                coletores = cursor.fetchall()
                if coletores:
                    print("\n=== Coletores Cadastrados ===")
                    headers = ["ID Coletor", "Nome", "CNPJ/CPF", "Telefone", "Endereço", "Nome Cidade", "Data Cadastro"]
                    print(tabulate(coletores, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhum coletor cadastrado.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")

    def atualizar_coletor(self, idcoletor, cidade_idcidade, novo_nome, novo_cnpjCpf, novo_telefone, novo_endereco, nova_dataCadastro):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                UPDATE coletor 
                SET nome = %s, cnpjCpf = %s, telefone = %s, endereco = %s, dataCadastro = %s 
                WHERE idcoletor = %s AND cidade_idcidade = %s
                """
                cursor.execute(sql_query, (novo_nome, novo_cnpjCpf, novo_telefone, novo_endereco, nova_dataCadastro, idcoletor, cidade_idcidade))
                self.connection.commit()
                print(f"Coletor ID {idcoletor} atualizado.")
            except Error as e:
                print(f"Erro ao atualizar dados: {e}")

    def excluir_coletor(self, idcoletor, cidade_idcidade):
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM coletor WHERE idcoletor = %s AND cidade_idcidade = %s"
                cursor.execute(sql_query, (idcoletor, cidade_idcidade))
                self.connection.commit()
                print(f"Coletor ID {idcoletor} excluído com sucesso!")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")

# Funções de interface para o menu de coletores
def cadastrar_coletor(db_coletor):
    nome = input("Digite o nome do coletor: ")
    cnpjCpf = input("Digite o CNPJ ou CPF do coletor: ")
    telefone = input("Digite o telefone do coletor: ")
    endereco = input("Digite o endereço do coletor: ")
    cidade_idcidade = int(input("Digite o ID da cidade do coletor: "))
    dataCadastro = input("Digite a data de cadastro (YYYY-MM-DD): ")
    db_coletor.inserir_coletor(nome, cnpjCpf, telefone, endereco, cidade_idcidade, dataCadastro)

def editar_coletor(db_coletor):
    idcoletor = int(input("Digite o ID do coletor que deseja editar: "))
    cidade_idcidade = int(input("Digite o ID da cidade do coletor: "))
    novo_nome = input("Digite o novo nome do coletor: ")
    novo_cnpjCpf = input("Digite o novo CNPJ ou CPF do coletor: ")
    novo_telefone = input("Digite o novo telefone do coletor: ")
    novo_endereco = input("Digite o novo endereço do coletor: ")
    nova_dataCadastro = input("Digite a nova data de cadastro (YYYY-MM-DD): ")
    db_coletor.atualizar_coletor(idcoletor, cidade_idcidade, novo_nome, novo_cnpjCpf, novo_telefone, novo_endereco, nova_dataCadastro)

def excluir_coletor(db_coletor):
    idcoletor = int(input("Digite o ID do coletor que deseja excluir: "))
    cidade_idcidade = int(input("Digite o ID da cidade do coletor: "))
    db_coletor.excluir_coletor(idcoletor, cidade_idcidade)