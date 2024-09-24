class TipoResiduo:
    def __init__(self, nome, unidade_medida):
        self.__nome = nome  # Nome do tipo de resíduo
        self.__unidade_medida = unidade_medida  # Unidade de medida do resíduo

    def validar_quantidade(self, quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa!")
        return quantidade  # Retorna a quantidade se não for menor que 0
        
    def get_nome(self):
        return self.__nome  # Retorna o nome do tipo de resíduo

    def get_unidade_medida(self):
        return self.__unidade_medida  # Retorna a unidade de medida do resíduo


class Usuario:
    def __init__(self, nome, cpf=None):
        self.__nome = nome  # Nome do usuário
        self.__cpf = cpf  # CPF do usuário (opcional)
        self.__residuos_coletados = []  # Lista de resíduos coletados pelo usuário

    def adicionar_residuos(self, tipo_residuo, quantidade):
        # Adiciona um resíduo coletado à lista
        self.__residuos_coletados.append((tipo_residuo.get_nome(), quantidade))

    def get_nome(self):
        return self.__nome  # Retorna o nome do usuário

    def get_cpf(self):
        return self.__cpf  # Retorna o CPF do usuário

    def get_residuos_coletados(self):
        return self.__residuos_coletados  # Retorna a lista de resíduos coletados


class LocalColeta:
    def __init__(self, nome, endereco):
        self.__nome = nome  # Nome do local de coleta
        self.__endereco = endereco  # Endereço do local de coleta

    def get_nome(self):
        return self.__nome  # Retorna o nome do local de coleta

    def get_endereco(self):
        return self.__endereco  # Retorna o endereço do local de coleta


class AgendamentoColeta:
    def __init__(self, data_hora, tipo_residuo, usuario):
        self.__data_hora = data_hora  # Data e hora do agendamento
        self.__tipo_residuo = tipo_residuo  # Tipo de resíduo a ser coletado
        self.__usuario = usuario  # Usuário que agendou a coleta

    def exibir_agendamento(self):
        # Exibe as informações do agendamento
        print(f"Agendamento: Coleta de {self.__tipo_residuo.get_nome()} na data/hora {self.__data_hora} por {self.__usuario.get_nome()}")


class Coleta:
    def __init__(self, tipo_residuo, quantidade, usuario, local_coleta):
        self.__tipo_residuo = tipo_residuo  # Tipo de resíduo coletado
        self.__quantidade = quantidade  # Quantidade de resíduo coletado
        self.__usuario = usuario  # Usuário que fez a coleta
        self.__local_coleta = local_coleta  # Local onde a coleta foi feita

    def registrar_coleta(self):
        # Registra a coleta e atualiza o histórico do usuário
        quantidade_calculada = self.__tipo_residuo.validar_quantidade(self.__quantidade)
        self.__usuario.adicionar_residuos(self.__tipo_residuo, quantidade_calculada)
        print(f'Coleta registrada: {quantidade_calculada} {self.__tipo_residuo.get_unidade_medida()} de {self.__tipo_residuo.get_nome()} por {self.__usuario.get_nome()} no {self.__local_coleta.get_nome()}.')


class SistemaColeta:
    def __init__(self):
        self.__usuarios = []  # Lista de usuários cadastrados
        self.__coletas = []  # Lista de coletas registradas
        self.__locais_coleta = []  # Lista de locais de coleta
        self.__agendamentos = []  # Lista de agendamentos de coleta
        self.__ranking = {}  # Dicionário para armazenar o ranking dos usuários

    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)  # Adiciona um usuário ao sistema
        self.__ranking[usuario.get_nome()] = 0  # Inicializa o ranking do usuário

    def adicionar_local_coleta(self, local_coleta):
        self.__locais_coleta.append(local_coleta)  # Adiciona um local de coleta ao sistema

    def registrar_coleta(self, tipo_residuo, quantidade, usuario, local_coleta):
        # Cria uma nova coleta e registra
        coleta = Coleta(tipo_residuo, quantidade, usuario, local_coleta)
        coleta.registrar_coleta()
        self.__coletas.append(coleta)  # Adiciona a coleta à lista de coletas
        self.atualizar_ranking(usuario)  # Atualiza o ranking do usuário

    def agendar_coleta(self, data_hora, tipo_residuo, usuario):
        # Cria um agendamento de coleta
        agendamento = AgendamentoColeta(data_hora, tipo_residuo, usuario)
        self.__agendamentos.append(agendamento)  # Adiciona o agendamento à lista
        agendamento.exibir_agendamento()  # Exibe as informações do agendamento

    def atualizar_ranking(self, usuario):
        # Atualiza o ranking do usuário com base nos resíduos coletados
        total = sum(q for _, q in usuario.get_residuos_coletados())
        self.__ranking[usuario.get_nome()] = total  # Atualiza o total no ranking

    def exibir_ranking(self):
        # Exibe o ranking dos usuários ordenado pela quantidade de resíduos coletados
        ranking_ordenado = sorted(self.__ranking.items(), key=lambda x: x[1], reverse=True)
        print("\nRanking dos usuários:")
        for posicao, (nome, total_residuos) in enumerate(ranking_ordenado, start=1):
            print(f"{posicao}. {nome}: {total_residuos}g coletados")

    def relatorio_residuos(self):
        # Gera um relatório da quantidade de resíduos coletados por tipo
        relatorio = {}
        for coleta in self.__coletas:
            tipo = coleta._Coleta__tipo_residuo.get_nome()  # Acessa o tipo de resíduo da coleta
            if tipo not in relatorio:
                relatorio[tipo] = 0
            relatorio[tipo] += coleta._Coleta__quantidade  # Acumula a quantidade

        print("\nRelatório de Resíduos Coletados:")
        for tipo, quantidade in relatorio.items():
            print(f"{tipo}: {quantidade}g")

    def visualizar_residuos_usuario(self, usuario):
        # Exibe os resíduos coletados por um usuário específico
        print(f"\nResíduos coletados por {usuario.get_nome()}:")
        for tipo, quantidade in usuario.get_residuos_coletados():
            print(f"{tipo}: {quantidade}g")
            

def menu():
    print('''
    ============== SISTEMA DE COLETA SELETIVA ==============
    '''
)


def executar_sistema():
    menu()

    papel = TipoResiduo("Papel", "gramas")
    plastico = TipoResiduo("Plástico", "gramas")  # Instâncias
    metal = TipoResiduo("Metal", "gramas")

    usuario1 = Usuario("Gustavo", "123.456.789-10")  # Instâncias
    usuario2 = Usuario("Calebe", "987.654.321-00")
    empresa1 = Usuario("Empresa Recicla", "823.920.332-11")
    empresa2 = Usuario("Reciclogenio", "023.112.942-23")

    supermercado_a = LocalColeta("SempreVale A", "Rua 1, 123")  # Instâncias
    mercado_b = LocalColeta("SempreVale B", "Rua 2, 456")

    sistema = SistemaColeta()

    sistema.adicionar_usuario(usuario1)  # Adiciona o usuário Gustavo ao sistema
    sistema.adicionar_usuario(usuario2)  # Adiciona o usuário Calebe ao sistema

    sistema.adicionar_local_coleta(supermercado_a)  # Adiciona o SempreVale A ao sistema
    sistema.adicionar_local_coleta(mercado_b)  # Adiciona o SempreVale B ao sistema

    sistema.registrar_coleta(papel, 120, usuario1, supermercado_a)  # Registra a coleta de papel
    sistema.registrar_coleta(plastico, 250, usuario2, mercado_b)  # Registra a coleta de plástico
    sistema.registrar_coleta(metal, 650, usuario1, supermercado_a)  # Registra a coleta de metal

    sistema.agendar_coleta("2024-10-01 10:00", papel, empresa1)  # Agenda coleta de papel para Empresa Recicla
    sistema.agendar_coleta("2024-10-02 14:00", plastico, empresa2)  # Agenda coleta de plástico para Reciclogenio

    sistema.exibir_ranking()  # Exibe o ranking dos usuários
    sistema.relatorio_residuos()  # Gera o relatório de resíduos coletados
    sistema.visualizar_residuos_usuario(usuario1)  # Exibe resíduos coletados por Gustavo
    sistema.visualizar_residuos_usuario(usuario2)  # Exibe resíduos coletados por Calebe


if __name__ == "__main__":
    executar_sistema()  # Executa o sistema
