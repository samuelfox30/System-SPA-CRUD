class Contato:
    def __init__(self, nome, email, endereco, telefone):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        print(f'\n\nObjeto de Login criado:\nNome: {self.nome}\nEmail: {self.email}\nEndereco: {self.endereco}\nTelefone: {self.telefone}\n\n')
        return f'Nome:{self.nome}Email:{self.email}Endereco:{self.endereco}Telefone:{self.telefone}'
