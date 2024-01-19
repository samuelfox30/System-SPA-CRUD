import sqlite3


class SystemDatabase:

    database_name = '../contacts.db'

    def __init__(self, user):
        try:
            self.conn = sqlite3.connect(SystemDatabase.database_name)
            self.cursor = self.conn.cursor()  # Criando cursor
            self.comando = f'CREATE TABLE IF NOT EXISTS {user} (ID INTEGER PRIMARY KEY, NOME VARCHAR(60), EMAIL VARCHAR(100), ENDERECO VARCHAR(130), TELEFONE VARCHAR(20))'
            self.cursor.execute(self.comando)
            print(f"\n\nConexão estabelecida com banco: {SystemDatabase.database_name}\n\n")
        except Exception as error:
            print(f'\n\nOcorreu um erro ao estabelecer uma conexão com o banco: {SystemDatabase.database_name}\n\n')

    def teste(self):
        pass