import sqlite3


class SystemDatabase:

    database_name = '../system.db'

    def __init__(self):
        try:
            self.conn = sqlite3.connect(SystemDatabase.database_name)
            self.cursor = self.conn.cursor()  # Criando cursor
            self.comando = 'CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY, NOME VARCHAR(60), EMAIL VARCHAR(100), SENHA VARCHAR(30))'
            self.cursor.execute(self.comando)
            print(f"\n\nConexão estabelecida com banco: {SystemDatabase.database_name}\n\n")
        except Exception as error:
            print(f'\n\nOcorreu um erro ao estabelecer uma conexão com o banco: {SystemDatabase.database_name}\n\n')


    def verificar_existencia(self, user):
        try:
            email = user.email
            self.cursor.execute('SELECT * FROM USERS WHERE EMAIL = ?', (email,))
            result = self.cursor.fetchone()
            if not result:
                return True
            else:
                return False
        except Exception as error:
            print(f'Ocorreu um erro ao verificar a existência de um email: {error}')
            return False
        finally:
            self.conn.commit()


    def cadastrar(self, user):
        try:
            nome = user.nome
            email = user.email
            senha = user.senha
            self.cursor.execute('INSERT INTO USERS (NOME, EMAIL, SENHA) VALUES (?, ?, ?)',(nome, email, senha))
            print('\n\nCadastro realizado com sucesso!\n\n')
        except Exception as error:
            print(f'\n\nOcorreu um erro ao tentar cadastrar o usuario: \n{nome}\n{email}\n{senha}\n\n')
        finally:
            self.conn.commit()
            # Exibindo dados:
            self.cursor.execute('SELECT * FROM USERS')
            linhas = self.cursor.fetchall()
            for linha in linhas:
                print(linha)


    def permitir_login(self, user):
        try:
            email = user.email
            senha = user.senha
            self.cursor.execute('SELECT * FROM USERS WHERE EMAIL = ?', (email,))
            result = self.cursor.fetchone()
            email_original = str(result[2])
            senha_original = str(result[3])

            # ------- LOGADO:
            if email == email_original and senha == senha_original:
                return True
            # ------- NÃO LOGADO:
            else:
                return False
                
        except Exception as error:
            print(f'\n\nOcorreu um erro na tentativa de verificar o login do usuario: \n{email}\n{senha}\n\n')
            return False
        finally:
            self.conn.commit()
            # Exibindo dados:
            self.cursor.execute('SELECT * FROM USERS')
            linhas = self.cursor.fetchall()
            for linha in linhas:
                print(linha)