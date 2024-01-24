class UserCadastro:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        print(f'\n\nObjeto de Cadastro criado:\nNome: {self.nome}\nEmail: {self.email}\nSenha: {self.senha}\n\n')
        return f'Usuário de Cadastro: Nome={self.nome}, Email={self.email}, Senha={self.senha}'


class UserLogin:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __str__(self):
        print(f'\n\nObjeto de Login criado:\nEmail: {self.email}\nSenha: {self.senha}\n\n')
        return f'Usuário de Login: Email={self.email}, Senha={self.senha}'
