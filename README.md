# Sistema Recicla

Projeto Integrado (P.I.) desenvolvido para a disciplina de Modelagem de Dados, com o objetivo de criar um sistema de gestão de resíduos recicláveis. Este sistema permite o cadastro, atualização, visualização e exclusão de tipos de usuários, usuários, categorias e materiais recicláveis. **Tecnologias principais**: Python, MySQL, Power BI.

## Sumário

- [Funcionalidades](#funcionalidades)
- [Arquitetura e Estrutura do Banco de Dados](#arquitetura-e-estrutura-do-banco-de-dados)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Instalação e Execução](#instalação-e-execução)
- [Uso do Sistema](#uso-do-sistema)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Funcionalidades

O sistema foi projetado para gerenciar informações sobre tipos de usuário, usuários, categorias de resíduos recicláveis e materiais. As principais funcionalidades incluem:

- **Inserir Dados**:
  - Cadastrar tipos de usuários, novos usuários, categorias e materiais.
- **Atualizar Dados**:
  - Editar informações de tipos de usuários, usuários, categorias e materiais.
- **Excluir Dados**:
  - Remover tipos de usuários, usuários, categorias e materiais do sistema.
- **Mostrar Dados**:
  - Visualizar todos os tipos de usuários, usuários, categorias e materiais cadastrados.

## Arquitetura e Estrutura do Banco de Dados

- **Banco de Dados**: MySQL
  - **Tabelas**:
    - `usuario`: Armazena informações dos usuários cadastrados no sistema.
    - `tipoUsuario`: Armazena tipos de perfis de usuário (ex.: administrador, colaborador).
    - `categoria`: Armazena as categorias de lixos recicláveis (ex.: plástico, papel).
    - `material`: Armazena os materiais e suas respectivas categorias.
  - **Views**: Criadas para integração com Power BI e visualização de dados gerenciais.
  - **Índices**: Implementados para otimização das consultas.

- **Tecnologias**:
  - **Linguagem de Programação**: Python, com uso de Programação Orientada a Objetos.
  - **Ferramentas**:
    - **VSCode**: Ambiente de desenvolvimento.
    - **GitHub**: Repositório de código-fonte.
    - **Power BI**: Integração para visualização de dados.

## Configuração do Ambiente

Para configurar o ambiente de desenvolvimento:

1. **Instale o MySQL**:
   - **Host**: `localhost`
   - **Usuário**: `root`
   - **Senha**: `1234`

2. **Crie as tabelas** no MySQL:
   - Scripts SQL estão disponíveis na pasta `/Banco de Dados` do repositório.

3. **Instale as bibliotecas necessárias em Python**:
   - Execute `pip install -r requirements.txt` para instalar as dependências.

## Instalação e Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sistema-recicla.git
   ```
2. **Navegue até o diretório do projeto**:
   ```bash
   cd sistema-recicla
   ```
3. **Configure o banco de dados**:
   - Execute os scripts SQL para criar as tabelas e views necessárias.

4. **Execute o sistema**:
   ```bash
   python main.py
   ```

## Uso do Sistema

- **Fluxo de Menus**:
  - **Inserir**: Cadastrar tipo de usuário, cadastrar usuário, cadastrar categoria, cadastrar material.
  - **Atualizar**: Editar tipo de usuário, editar usuário, editar categoria, editar material.
  - **Excluir**: Excluir tipo de usuário, excluir usuário, excluir categoria, excluir material.
  - **Mostrar**: Mostrar tipo de usuário, mostrar usuário, mostrar categoria, mostrar material.

Para mais detalhes sobre cada funcionalidade, consulte o manual do usuário localizado na pasta `/docs` do repositório.

## Contribuição

Para contribuir com o projeto:

1. Realize um **fork** do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Faça o commit de suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie a sua branch (`git push origin feature/nova-funcionalidade`).
5. Abra um **Pull Request**.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
