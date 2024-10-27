import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

class AgendamentoDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def conectar(self):
        """Estabelece conexão com o banco de dados."""
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
        """Encerra a conexão com o banco de dados."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")

    def inserir_agendamento(self, data, hora, status, coletor_idcoletor):
        """Insere um novo agendamento no banco de dados."""
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "INSERT INTO agendamento (data, hora, status, coletor_idcoletor) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_query, (data, hora, status, coletor_idcoletor))
                self.connection.commit()
                print(f"Agendamento para o coletor ID {coletor_idcoletor} inserido com sucesso!")
            except Error as e:
                print(f"Erro ao inserir dados: {e}")
            finally:
                cursor.close()  

    def listar_agendamentos(self):
        """Lista todos os agendamentos armazenados no banco de dados."""
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    SELECT 
                        agendamento.idagendamento, 
                        agendamento.data, 
                        agendamento.hora, 
                        agendamento.status, 
                        coletor.nome AS nome_coletor 
                    FROM 
                        agendamento 
                    INNER JOIN 
                        coletor ON agendamento.coletor_idcoletor = coletor.idcoletor
                """)
                agendamentos = cursor.fetchall()
                if agendamentos:
                    print("\n=== Agendamentos ===")
                    headers = ["ID Agendamento", "Data", "Hora", "Status", "Nome Coletor"]
                    print(tabulate(agendamentos, headers=headers, tablefmt="grid"))
                else:
                    print("Nenhum agendamento encontrado.")
            except Error as e:
                print(f"Erro ao buscar dados: {e}")
            finally:
                cursor.close()  

    def editar_agendamento(self, idagendamento, novos_dados):
        """Edita um agendamento específico no banco de dados."""
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = """
                    UPDATE agendamento 
                    SET data = %s, hora = %s, status = %s, coletor_idcoletor = %s 
                    WHERE idagendamento = %s
                """
                cursor.execute(sql_query, (novos_dados['data'], novos_dados['hora'], novos_dados['status'], novos_dados['coletor_idcoletor'], idagendamento))
                self.connection.commit()
                if cursor.rowcount > 0:
                    print(f"Agendamento ID {idagendamento} atualizado com sucesso!")
                else:
                    print(f"Nenhum agendamento encontrado com o ID {idagendamento}.")
            except Error as e:
                print(f"Erro ao editar dados: {e}")
            finally:
                cursor.close()  

    def excluir_agendamento(self, idagendamento):
        """Exclui um agendamento específico do banco de dados."""
        if self.connection is not None and self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql_query = "DELETE FROM agendamento WHERE idagendamento = %s"
                cursor.execute(sql_query, (idagendamento,))
                self.connection.commit()
                if cursor.rowcount > 0:
                    print(f"Agendamento ID {idagendamento} excluído com sucesso!")
                else:
                    print(f"Nenhum agendamento encontrado com o ID {idagendamento}.")
            except Error as e:
                print(f"Erro ao excluir dados: {e}")
            finally:
                cursor.close()  

# Funções de interface para o menu de agendamentos
def cadastrar_agendamento(db_agendamento):
    """Captura os dados do usuário e insere um novo agendamento."""
    data = input("Digite a data do agendamento (YYYY-MM-DD): ")
    hora = input("Digite a hora do agendamento (HH:MM:SS): ")
    status = input("Digite o status do agendamento (Pendente, Confirmado, Cancelado): ")
    coletor_idcoletor = int(input("Digite o ID do coletor: "))
    db_agendamento.inserir_agendamento(data, hora, status, coletor_idcoletor)

def listar_agendamentos(db_agendamento):
    """Lista os agendamentos existentes."""
    db_agendamento.listar_agendamentos()

def excluir_agendamento(db_agendamento):
    """Solicita o ID de um agendamento e o exclui."""
    idagendamento = int(input("Digite o ID do agendamento que deseja excluir: "))
    db_agendamento.excluir_agendamento(idagendamento)

def editar_agendamento(db_agendamento):
    """Solicita o ID de um agendamento e novos dados para edição."""
    idagendamento = int(input("Digite o ID do agendamento que deseja editar: "))
    novos_dados = {}
    novos_dados['data'] = input("Digite a nova data do agendamento (YYYY-MM-DD): ")
    novos_dados['hora'] = input("Digite a nova hora do agendamento (HH:MM:SS): ")
    novos_dados['status'] = input("Digite o novo status do agendamento (Pendente, Confirmado, Cancelado): ")
    novos_dados['coletor_idcoletor'] = int(input("Digite o novo ID do coletor: "))
    db_agendamento.editar_agendamento(idagendamento, novos_dados)