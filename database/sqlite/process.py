import sqlite3


class SystemDatabase:

    database_name = '../system.db'

    def __init__(self):
        try:
            self.conn = sqlite3.connect(SystemDatabase.database_name)
            self.cursor = self.conn.cursor()
            self.comando = 'CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY, NOME VARCHAR(60), EMAIL VARCHAR(50), SENHA VARCHAR(30))'
            self.cursor.execute(self.comando)
            print(f"\n\nConexão estabelecida com banco: {SystemDatabase.database_name}\n\n")
        except Exception as error:
            print(f'\n\nOcorreu um erro ao estabelecer uma conexão com o banco: {SystemDatabase.database_name}\n\n')


    def verificar_existencia(self, user) -> bool:
        try:
            email = user.email
            self.cursor.execute('SELECT * FROM USERS WHERE EMAIL = ?', (email,))
            result = self.cursor.fetchone()
            if not result:
                return False
            else:
                return True
        except Exception as error:
            print(f'Ocorreu um erro ao verificar a existência de um email: {error}')
            return False
        finally:
            self.conn.commit()


    def cadastrar(self, user) -> bool:
        try:
            nome = user.nome
            email = user.email
            senha = user.senha
            self.cursor.execute('INSERT INTO USERS (NOME, EMAIL, SENHA) VALUES (?, ?, ?)',(nome, email, senha))
            print('\n\nCadastro realizado com sucesso!\n\n')
            return True
        except Exception as error:
            print(f'\n\nOcorreu um erro ao tentar cadastrar o usuario: \n{nome}\n{email}\n{senha}\n\n')
            return False
        finally:
            self.conn.commit()
            # Exibindo dados:
            self.cursor.execute('SELECT * FROM USERS')
            linhas = self.cursor.fetchall()
            for linha in linhas:
                print(linha)


    def permitir_login(self, user) -> bool:
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


    # ------ FUNÇÂO DE EXCLUSÃO MANUAL
    def excluir_manual(self, email) -> bool:
        try:
            self.cursor.execute('DELETE FROM USERS WHERE EMAIL = ?', (email,))
            print(f'Usuário com o email {email} excluído com sucesso.')
            return True
        except Exception as error:
            print(f'Ocorreu um erro ao excluir o usuário:\n{error}')
            return False
        finally:
            self.conn.commit()


class ContactsDatabase:

    database_name = '../contacts.db'

    def __init__(self, sessao):
        try:
            self.sessao = sessao
            self.conn = sqlite3.connect(ContactsDatabase.database_name)
            self.cursor = self.conn.cursor()
            self.comando = f'CREATE TABLE IF NOT EXISTS {self.sessao} (ID INTEGER PRIMARY KEY, NOME VARCHAR(60), EMAIL VARCHAR(50), ENDERECO VARCHAR(100), TELEFONE VARCHAR(20))'
            self.cursor.execute(self.comando)
            print(f"\n\nConexão estabelecida com banco: {ContactsDatabase.database_name}\n\n")
        except Exception as error:
            print(f'\n\nOcorreu um erro ao estabelecer uma conexão com o banco: {error}\n\n')


    def exibir(self):
        try:
            contatos = []
            self.cursor.execute(f'SELECT * FROM {self.sessao}')
            linhas = self.cursor.fetchall()
            for linha in linhas:
                contatos.append(linha)
            return contatos
        except Exception as error:
            print(f'\n\nOcorreu um erro ao exibir os contatos: {error}\n\n')
            return False
        finally:
            self.conn.commit()


    def adicionar(self, contato) -> bool:
        try:
            nome = contato.nome
            email = contato.email
            endereco = contato.endereco
            telefone = contato.telefone
            self.cursor.execute(f'INSERT INTO {self.sessao} (NOME, EMAIL, ENDERECO, TELEFONE) VALUES (?, ?, ?, ?)',(nome, email, endereco, telefone))
            print('\n\nContato adicionado com sucesso!\n\n')
            return True
        except Exception as error:
            print(f'\n\nOcorreu um erro ao tentar adicionar um contato: {error}\n\n')
            return False
        finally:
            self.conn.commit()


    def excluir(self, id) -> bool:
        try:
            self.cursor.execute(f"DELETE FROM {self.sessao} WHERE ID=?", (id,))
            print(f'Contato excluido com sucesso')
            return True
        except Exception as error:
            print(f'\n\nOcorreu um erro ao excluir um contato: {error}\n\n')
            return False
        finally:
            self.conn.commit()


    def editar(self, id, contato) -> bool:
        try:
            novo_nome = contato.nome
            novo_email = contato.email
            novo_endereco = contato.endereco
            novo_telefone = contato.telefone
            self.cursor.execute(f'UPDATE {self.sessao} SET NOME=?, EMAIL=?, ENDERECO=?, TELEFONE=? WHERE ID=?',(novo_nome, novo_email, novo_endereco, novo_telefone, id))
            print(f'Contato editado com sucesso')
            return True
        except Exception as error:
            print(f'\n\nOcorreu um erro ao editar um contato: {error}\n\n')
            return False
        finally:
            self.conn.commit()


    def pesquisar(self, dado):
        try:
            self.cursor.execute(f'SELECT * FROM {self.sessao} WHERE NOME = ? OR EMAIL = ? OR ENDERECO = ? OR SENHA = ?', (dado, dado, dado, dado))
            result = self.cursor.fetchall()
            if not result:
                return False
            else:
                return result
        except Exception as error:
            print(f'Ocorreu um erro ao pesquisar por um dado: {error}')
            return False
        finally:
            self.conn.commit()