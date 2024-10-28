# Sistema Recicla

## Descrição do Projeto
O **Sistema Recicla** é um sistema de gerenciamento de materiais recicláveis desenvolvido como parte do Projeto Integrado (P.I.) para o curso universitário. Este sistema permite o cadastro, atualização, exibição e exclusão de usuários, categorias de lixo reciclável e materiais. Além disso, integra-se com o Power BI para uma análise visual das informações cadastradas, facilitando a gestão e o entendimento dos dados.

## Funcionalidades Principais
- **Cadastro e Gestão de Usuários:** Permite o cadastro de novos usuários, a edição e a exclusão de usuários existentes, e a classificação dos usuários em diferentes tipos.
- **Gestão de Categorias de Lixo Reciclável:** Possibilita o cadastro, exibição, edição e exclusão de categorias de materiais recicláveis.
- **Gestão de Materiais Recicláveis:** Registra e mantém informações detalhadas sobre materiais recicláveis.
- **Integração com Power BI:** Utiliza views específicas no banco de dados para conectar o Power BI e possibilitar uma visualização prática e eficiente das informações cadastradas.
- **Interface Intuitiva em Menu:** Navegação simplificada para a inserção, atualização, exclusão e visualização de registros.

## Estrutura do Menu
1. **Inserir**
   - Cadastrar tipo de usuário
   - Cadastrar usuário
   - Cadastrar categoria
   - Cadastrar material
   - Voltar ao menu principal

2. **Atualizar**
   - Editar tipo de usuário
   - Editar usuário
   - Editar categoria
   - Editar material
   - Voltar ao menu principal

3. **Excluir**
   - Excluir tipo de usuário
   - Excluir usuário
   - Excluir categoria
   - Excluir material
   - Voltar ao menu principal

4. **Mostrar**
   - Mostrar tipo de usuário
   - Mostrar usuário
   - Mostrar categoria
   - Mostrar material
   - Voltar ao menu principal

5. **Sair**

## Estrutura do Banco de Dados
O banco de dados foi implementado em **MySQL** com a seguinte estrutura:
- **Tabelas principais:** `usuario`, `tipoUsuario`, `categoria`, e `material`.
- **Índices e Views:** Implementados para otimização de consultas e integração com Power BI.

**Configurações de Conexão:**
- **Host:** localhost
- **Usuário:** root
- **Senha:** 1234

## Tecnologias Utilizadas
- **Linguagem:** Python, utilizando programação orientada a objetos (POO).
- **Banco de Dados:** MySQL, com o uso de views para a integração com Power BI.
- **Ferramenta de Visualização:** Power BI.
- **IDE:** Visual Studio Code.
- **Versionamento de Código:** GitHub.

## Professores Orientadores
Este projeto contou com o apoio e orientação dos seguintes professores:
- **Mariangela Martimbianco Santos:** Power BI
- **Max Streicher Vallim:** Modelagem de Dados
- **Nivaldo de Andrade:** Programação Orientada a Objetos
- **Marcelo Ciacco de Almeida:** Lógica de Programação

## Como Executar o Projeto
1. **Clonar o Repositório:**
   ```bash
   https://github.com/marciopro3/pi_2semestre
   ```
2. **Configurar o Banco de Dados:** Criar as tabelas no MySQL utilizando os scripts fornecidos e configurar o arquivo de conexão com os detalhes do banco de dados.
3. **Executar o Sistema:** Execute o script principal do projeto com:
   ```bash
   python main.py
   ```
4. **Visualização dos Dados no Power BI:** Conectar o Power BI ao banco de dados MySQL e utilizar as views pré-configuradas para análise.

---

**Projeto desenvolvido para fins acadêmicos.**
