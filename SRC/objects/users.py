class UserCadastro:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'Usuário de Cadastro: Nome={self.nome}, Email={self.email}, Senha={self.senha}'


class UserLogin:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'Usuário de Login: Email={self.email}, Senha={self.senha}'
