import sqlite3
import re


class SystemDatabase:

    database_name = '../contacts.db'

    def __init__(self, user):
        try:
            self.user = re.sub(r'[^a-zA-Z0-9._]', '', user)
            self.conn = sqlite3.connect(SystemDatabase.database_name)
            self.cursor = self.conn.cursor()
            self.comando = f'CREATE TABLE IF NOT EXISTS {self.user} (ID INTEGER PRIMARY KEY, NOME VARCHAR(60), EMAIL VARCHAR(100), ENDERECO VARCHAR(130), TELEFONE VARCHAR(20))'
            self.cursor.execute(self.comando)
            print(f"\n\nConexão estabelecida com banco: {SystemDatabase.database_name}\n\n")
        except Exception as error:
            print(f'\n\nOcorreu um erro ao estabelecer uma conexão com o banco: {error}\n\n')

    def cadastrar(self, user):
        try:
            usuario_logado = self.user
            nome = user.nome
            email = user.email
            endereco = user.endereco
            telefone = user.telefone
            self.cursor.execute(f'INSERT INTO {usuario_logado} (NOME, EMAIL, ENDERECO, TELEFONE) VALUES (?, ?, ?, ?)',(nome, email, endereco, telefone))
            print('\n\nCadastro realizado com sucesso!\n\n')
        except Exception as error:
            print(f'\n\nOcorreu um erro ao tentar cadastrar o contato: {error}\n\n')
        finally:
            self.conn.commit()
            # Exibindo dados:
            self.cursor.execute(f'SELECT * FROM {usuario_logado}')
            linhas = self.cursor.fetchall()
            for linha in linhas:
                print(linha)
        