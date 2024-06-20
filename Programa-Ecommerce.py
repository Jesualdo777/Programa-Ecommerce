# Importa a biblioteca mysql.connector para conectar e interagir com um banco de dados MySQL.
import mysql.connector

# Define a classe Usuario com atributos relacionados a um usuário.
class Usuario:
    def __init__(self, nome_usuario, email, senha_hash):
        self.nome_usuario = nome_usuario  # Inicializa o atributo nome_usuario.
        self.email = email  # Inicializa o atributo email.
        self.senha_hash = senha_hash  # Inicializa o atributo senha_hash.

# Define a classe Cliente com atributos relacionados a um cliente.
class Cliente:
    def __init__(self, primeiro_nome, sobrenome, telefone, data_nascimento):
        self.primeiro_nome = primeiro_nome  # Inicializa o atributo primeiro_nome.
        self.sobrenome = sobrenome  # Inicializa o atributo sobrenome.
        self.telefone = telefone  # Inicializa o atributo telefone.
        self.data_nascimento = data_nascimento  # Inicializa o atributo data_nascimento.

# Define a classe Produto com atributos relacionados a um produto.
class Produto:
    def __init__(self, nome, descricao, preco, estoque):
        self.nome = nome  # Inicializa o atributo nome.
        self.descricao = descricao  # Inicializa o atributo descricao.
        self.preco = preco  # Inicializa o atributo preco.
        self.estoque = estoque  # Inicializa o atributo estoque.

# Define a classe SistemaEcommerce que gerencia a conexão com o banco de dados e as operações CRUD.
class SistemaEcommerce:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',  # Endereço do servidor de banco de dados.
            user='root',  # Nome de usuário para a conexão.
            password='he182555@',  # Senha do usuário.
            database='ecommerce_simple'  # Nome do banco de dados a ser utilizado.
        )
        self.cursor = self.conexao.cursor()  # Cria um cursor para executar comandos SQL.
        print("Conexão bem-sucedida ao banco de dados.")  # Informa que a conexão foi estabelecida com sucesso.

    # Método para adicionar um usuário no banco de dados.
    def adicionar_usuario(self, usuario):
        sql = 'INSERT INTO Usuarios (nome_usuario, email, senha_hash) VALUES (%s, %s, %s)'  # Define o comando SQL para inserir um novo usuário.
        valores = (usuario.nome_usuario, usuario.email, usuario.senha_hash)  # Cria uma tupla com os valores a serem inseridos.
        self.cursor.execute(sql, valores)  # Executa o comando SQL com os valores fornecidos.
        self.conexao.commit()  # Confirma a transação no banco de dados.
        print('Usuário adicionado com sucesso.')  # Imprime uma mensagem de sucesso.

    # Método para adicionar um cliente no banco de dados.
    def adicionar_cliente(self, cliente):
        sql = 'INSERT INTO Clientes (primeiro_nome, sobrenome, telefone, data_nascimento) VALUES (%s, %s, %s, %s)'  # Define o comando SQL para inserir um novo cliente.
        valores = (cliente.primeiro_nome, cliente.sobrenome, cliente.telefone, cliente.data_nascimento)  # Cria uma tupla com os valores a serem inseridos.
        self.cursor.execute(sql, valores)  # Executa o comando SQL com os valores fornecidos.
        self.conexao.commit()  # Confirma a transação no banco de dados.
        print('Cliente adicionado com sucesso.')  # Imprime uma mensagem de sucesso.

    # Método para adicionar um produto no banco de dados.
    def adicionar_produto(self, produto):
        sql = 'INSERT INTO Produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)'  # Define o comando SQL para inserir um novo produto.
        valores = (produto.nome, produto.descricao, produto.preco, produto.estoque)  # Cria uma tupla com os valores a serem inseridos.
        self.cursor.execute(sql, valores)  # Executa o comando SQL com os valores fornecidos.
        self.conexao.commit()  # Confirma a transação no banco de dados.
        print('Produto adicionado com sucesso.')  # Imprime uma mensagem de sucesso.

    # Método para listar todos os usuários do banco de dados.
    def listar_usuarios(self):
        self.cursor.execute('SELECT nome_usuario, email FROM Usuarios')  # Executa o comando SQL para selecionar nome_usuario e email dos usuários.
        usuarios = self.cursor.fetchall()  # Recupera todos os resultados da consulta.
        for usuario in usuarios:  # Itera sobre cada usuário recuperado.
            print(f'Nome de Usuário: {usuario[0]}, Email: {usuario[1]}')  # Imprime os detalhes de cada usuário.

    # Método para listar todos os clientes do banco de dados.
    def listar_clientes(self):
        self.cursor.execute('SELECT primeiro_nome, sobrenome, telefone, data_nascimento FROM Clientes')  # Executa o comando SQL para selecionar primeiro_nome, sobrenome, telefone e data_nascimento dos clientes.
        clientes = self.cursor.fetchall()  # Recupera todos os resultados da consulta.
        for cliente in clientes:  # Itera sobre cada cliente recuperado.
            print(f'Nome: {cliente[0]} {cliente[1]}, Telefone: {cliente[2]}, Data de Nascimento: {cliente[3]}')  # Imprime os detalhes de cada cliente.

    # Método para listar todos os produtos do banco de dados.
    def listar_produtos(self):
        self.cursor.execute('SELECT nome, descricao, preco, estoque FROM Produtos')  # Executa o comando SQL para selecionar nome, descricao, preco e estoque dos produtos.
        produtos = self.cursor.fetchall()  # Recupera todos os resultados da consulta.
        for produto in produtos:  # Itera sobre cada produto recuperado.
            print(f'Nome: {produto[0]}, Descrição: {produto[1]}, Preço: {produto[2]}, Estoque: {produto[3]}')  # Imprime os detalhes de cada produto.

    # Método para fechar a conexão com o banco de dados.
    def fechar_conexao(self):
        self.cursor.close()  # Fecha o cursor.
        self.conexao.close()  # Fecha a conexão com o banco de dados.
        print("Conexão ao banco de dados fechada.")  # Informa que a conexão foi fechada com sucesso.

# Função para exibir o menu e obter a escolha do usuário.
def menu():
    print("\nSistema de E-commerce")
    print("1. Adicionar Usuário")
    print("2. Adicionar Cliente")
    print("3. Adicionar Produto")
    print("4. Listar Usuários")
    print("5. Listar Clientes")
    print("6. Listar Produtos")
    print("7. Sair")
    return input("Escolha uma opção: ")  # Retorna a opção escolhida pelo usuário.

# Função principal para interação com o usuário.
def main():
    sistema = SistemaEcommerce()  # Cria uma instância do sistema de e-commerce.

    while True:  # Loop infinito para exibir o menu e lidar com as escolhas do usuário.
        opcao = menu()  # Exibe o menu e obtém a escolha do usuário.

        if opcao == '1':  # Se a escolha for adicionar usuário.
            nome_usuario = input("Nome de usuário: ")  # Solicita o nome de usuário.
            email = input("Email: ")  # Solicita o email.
            senha_hash = input("Senha (hash): ")  # Solicita a senha (hash).
            usuario = Usuario(nome_usuario, email, senha_hash)  # Cria uma instância de Usuario com os dados fornecidos.
            sistema.adicionar_usuario(usuario)  # Adiciona o usuário no banco de dados.

        elif opcao == '2':  # Se a escolha for adicionar cliente.
            primeiro_nome = input("Primeiro Nome: ")  # Solicita o primeiro nome.
            sobrenome = input("Sobrenome: ")  # Solicita o sobrenome.
            telefone = input("Telefone: ")  # Solicita o telefone.
            data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")  # Solicita a data de nascimento.
            cliente = Cliente(primeiro_nome, sobrenome, telefone, data_nascimento)  # Cria uma instância de Cliente com os dados fornecidos.
            sistema.adicionar_cliente(cliente)  # Adiciona o cliente no banco de dados.

        elif opcao == '3':  # Se a escolha for adicionar produto.
            nome = input("Nome do Produto: ")  # Solicita o nome do produto.
            descricao = input("Descrição: ")  # Solicita a descrição do produto.
            preco = float(input("Preço: "))  # Solicita o preço do produto.
            estoque = int(input("Estoque: "))  # Solicita o estoque do produto.
            produto = Produto(nome, descricao, preco, estoque)  # Cria uma instância de Produto com os dados fornecidos.
            sistema.adicionar_produto(produto)  # Adiciona o produto no banco de dados.

        elif opcao == '4':  # Se a escolha for listar usuários.
            sistema.listar_usuarios()  # Lista todos os usuários do banco de dados.

        elif opcao == '5':  # Se a escolha for listar clientes.
            sistema.listar_clientes()  # Lista todos os clientes do banco de dados.

        elif opcao == '6':  # Se a escolha for listar produtos.
            sistema.listar_produtos()  # Lista todos os produtos do banco de dados.

        elif opcao == '7':  # Se a escolha for sair.
            sistema.fechar_conexao()  # Fecha a conexão com o banco de dados.
            print("Sistema encerrado.")  # Informa que o sistema foi encerrado.
            break  # Encerra o loop.

        else:  # Se a escolha for inválida.
            print("Opção inválida. Tente novamente.")  # Informa ao usuário que a opção é inválida.

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente (não importado como módulo).
    main()  # Chama a função principal para iniciar o programa.
