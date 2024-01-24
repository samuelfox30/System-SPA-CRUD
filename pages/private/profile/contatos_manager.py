import re


def adicionarcontato(nome, email, endereco, telefone, sessao):
    try:
        if not nome:
            return {'Status': False, 'Message': 'O mínimo para criar um contato é criar o nome'}
        else:
            from SRC.objects.contacts import Contato
            contato = Contato(nome, email, endereco, telefone)
            from database.sqlite.process import ContactsDatabase
            sessao_user = re.sub(r'[^a-zA-Z]', '', sessao)
            print(f'\n\n{sessao_user}')
            db_instance = ContactsDatabase(sessao_user)
            db_instance.adicionar(contato)
            return {'Status': True, 'Message': 'Cadastro adicionado com sucesso!'}
    except Exception as error:
        print(f'Erro ao cadastrar novo contato: {error}')
        return {'Status': False, 'Message': ''}