from utils.crud import *

class DepositoDB:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor
        
    def cadastrar_deposito(self, deposito):
        try:
            sql_query = """
                INSERT INTO deposito (nome, endereco, cep, cidade_idcidade, telefone, capacidadeMaxima, dataCadastro, horaAbertura, horaFechamento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                deposito.get_nome(),
                deposito.get_endereco(),
                deposito.get_cep(),
                deposito.get_idcidade(),
                deposito.get_telefone(),
                deposito.get_capacidadeMaxima(),
                deposito.get_dataCadastro(),
                deposito.get_horaAbertura(),
                deposito.get_horaFechamento()
            )
            self.cursor.execute(sql_query, valores)
            self.conexao.commit()
            print(f"\n[+] Depósito '{deposito.get_nome()}' cadastrado com sucesso!")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao cadastrar dados: {e}")

        
    def consultar_depositos(self):
        try:
            sql_query = """
            SELECT 
                deposito.iddeposito, 
                deposito.nome, 
                deposito.capacidadeMaxima, 
                deposito.dataCadastro, 
                deposito.horaAbertura, 
                deposito.horaFechamento, 
                cidade.nome
            FROM 
                deposito 
            INNER JOIN 
                cidade ON deposito.cidade_idcidade = cidade.idcidade
            ORDER BY iddeposito ASC
            """
            self.cursor.execute(sql_query)
            depositos = self.cursor.fetchall()
            if depositos:
                print("\n=== Depósitos Cadastrados ===")
                headers = ["ID", "Nome", "Capacidade", "Data Cadastro", "Abertura", "Fechamento", "Cidade"]
                print(tabulate(depositos, headers=headers, tablefmt="fancy_grid"))
            else:
                print("\n[!] Nenhum depósito cadastrado.")
        except Error as e:
            print(f"Erro ao buscar dados: {e}")


    def consultar_deposito_por_id(self, iddeposito):
        try:
            sql_query = """
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
                cidade.nome
            FROM 
                deposito 
            INNER JOIN 
                cidade ON deposito.cidade_idcidade = cidade.idcidade
            WHERE deposito.iddeposito = %s
            """
            self.cursor.execute(sql_query, (iddeposito,))
            deposito = self.cursor.fetchone()
            if deposito:
                print("\n=== Depósito Escolhido ===")
                headers = ["ID", "Nome", "Endereço", "CEP", "Telefone", "Capacidade Máxima(g)", "Data Cadastro", "Hora Abertura", "Hora Fechamento", "Cidade"]
                print(tabulate([deposito], headers=headers, tablefmt="fancy_grid"))
                return deposito
            else:
                print(f"[!] Nenhum depósito encontrado com o ID {iddeposito}.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        

    def atualizar_deposito(self, iddeposito, cidade_idcidade, novo_nome, novo_endereco, novo_cep, novo_telefone, nova_capacidadeMaxima, nova_dataCadastro, nova_horaAbertura, nova_horaFechamento):
        try:  
            sql_query = """
            UPDATE 
                deposito 
            SET 
                nome = %s, 
                endereco = %s, 
                cep = %s, 
                telefone = %s, 
                capacidadeMaxima = %s, 
                dataCadastro = %s, 
                horaAbertura = %s, 
                horaFechamento = %s 
            WHERE 
                iddeposito = %s 
            AND 
                cidade_idcidade = %s
            """
            self.cursor.execute(sql_query, (novo_nome, novo_endereco, novo_cep, novo_telefone, nova_capacidadeMaxima, nova_dataCadastro, nova_horaAbertura, nova_horaFechamento, iddeposito, cidade_idcidade))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Deposito ID {iddeposito} atualizado para '{novo_nome}' com sucesso.")
            else:
                print(f"Nenhum deposito com o ID {iddeposito}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao atualizar dados: {e}")


    def excluir_deposito(self, iddeposito):
        try:
            sql_query = "DELETE FROM deposito WHERE iddeposito = %s"
            self.cursor.execute(sql_query, (iddeposito,))
            self.conexao.commit()
            if self.cursor.rowcount > 0:
                print(f"\n[+] Deposito ID {iddeposito} excluído com sucesso!")
            else:
                print(f"Nenhum deposito com o ID {iddeposito}.")
        except Error as e:
            self.conexao.rollback()
            print(f"Erro ao excluir dados: {e}")
