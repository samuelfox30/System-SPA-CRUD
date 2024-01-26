class Contato:
    def __init__(self, nome, email, endereco, telefone):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f'Contato: Nome={self.nome}, Email={self.email}, Endereco={self.endereco}, Telefone={self.telefone}'