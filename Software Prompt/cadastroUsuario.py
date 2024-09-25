import mysql.connector

class CadastroUsuario:
    def __init__(self):
        # Conexão com o banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Admin123*",
            database="SBOReciclaSV"  # Nome do banco de dados
        )
        self.cursor = self.conexao.cursor()

    def cadastrar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        idade = input("Digite a idade do usuário: ")

        # Inserindo no banco de dados
        sql = "INSERT INTO usuarios (nome, email, idade) VALUES (%s, %s, %s)"
        valores = (nome, email, idade)
        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("\nUsuário cadastrado com sucesso!\n")

    def listar_usuarios(self):
        sql = "SELECT * FROM usuarios"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()

        if not resultado:
            print("\nNenhum usuário cadastrado.\n")
        else:
            print("\nLista de usuários cadastrados:\n")
            for i, (id, nome, email, idade) in enumerate(resultado, 1):
                print(f"Usuário {i}:")
                print(f"Nome: {nome}")
                print(f"Email: {email}")
                print(f"Idade: {idade}")
                print()

    def cadastrar_tipo_usuario(self):
        tipo = input("Digite o tipo de usuário: ")

        # Inserindo no banco de dados
        sql = "INSERT INTO tipoUsuario (tipo) VALUES (%s)"
        valores = (tipo,)
        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("\nTipo de usuário cadastrado com sucesso!\n")

    def listar_tipos_usuario(self):
        sql = "SELECT * FROM tipoUsuario"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()

        if not resultado:
            print("\nNenhum tipo de usuário cadastrado.\n")
        else:
            print("\nLista de tipos de usuários cadastrados:\n")
            for i, (idtipoUsuario, tipo) in enumerate(resultado, 1):
                print(f"Tipo {i}:")
                print(f"ID: {idtipoUsuario}")
                print(f"Tipo: {tipo}")
                print()