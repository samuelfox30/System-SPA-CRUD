import sqlite3

class SystemDatabase:

    def __init__(self, database_name):
        try:
            self.conn = sqlite3.connect(database_name)
            self.cursor = self.conn.cursor()
            print(f"\n\nConexão estabelecida com banco: {database_name}\n\n")
        except Exception as error:
            print(f'\n\nOcorreu um erro ao estabelecer uma conexão com o banco: {error}\n\n')

    def exibir_tudo(self):
        try:
            self.cursor.execute('SELECT * FROM USERS')
            linhas = self.cursor.fetchall()
            for linha in linhas:
                print(linha)
        except Exception as error:
            print(f'Ocorreu um erro ao exibir os dados do banco de dados: {error}')

    def verificar_existencia(self, email):
        try:
            self.cursor.execute('SELECT * FROM USERS WHERE EMAIL = ?', (email,))
            result = self.cursor.fetchone()
            if not result:
                print(f'O email {email} não existe')
            else:
                print(f'O email {email} existe: {str(result)}')
        except Exception as error:
            print(f'Ocorreu um erro ao verificar a existência de um email: {error}')

    def cadastrar(self, nome, email, senha):
        try:
            self.cursor.execute('INSERT INTO USERS (NOME, EMAIL, SENHA) VALUES (?, ?, ?)', (nome, email, senha))
            print('\n\nCadastro realizado com sucesso!\n\n')
        except Exception as error:
            print(f'\n\nOcorreu um erro ao tentar cadastrar o usuario: \n{nome}\n{email}\n{senha}\n\n')

    def permitir_login(self, email, senha):
        try:
            self.cursor.execute('SELECT * FROM USERS WHERE EMAIL = ?', (email,))
            result = self.cursor.fetchone()
            if result:
                email_original = str(result[2])
                senha_original = str(result[3])
                # ------- LOGADO:
                if email == email_original and senha == senha_original:
                    print(f'Simulação de login permitida!')
                    return True
                # ------- NÃO LOGADO:
                else:
                    print(f'Simulação de login NÃO permitida!')
                    return False
            else:
                print(f'Usuário com o email {email} não encontrado.')
                return False
        except Exception as error:
            print(f'Ocorreu um erro na tentativa de verificar o login do usuario: \n{email}\n{senha}\n\n')
            return False

    def excluir_manual(self, email):
        try:
            self.cursor.execute('DELETE FROM USERS WHERE EMAIL = ?', (email,))
            print(f'Usuário com o email {email} excluído com sucesso.')
        except Exception as error:
            print(f'Ocorreu um erro ao excluir o usuário:\n{error}')
        finally:
            self.conn.commit()

# ------- COMANDOS ------- #
database_system = '../system.db'
database_contacts = '../contacts.db'

db_instance = SystemDatabase(database_system)
db_instance.exibir_tudo()