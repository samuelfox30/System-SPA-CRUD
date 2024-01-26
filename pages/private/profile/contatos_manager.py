import re


def exibircontatos(sessao) -> list:
    sessao_user = re.sub(r'[^a-zA-Z]', '', sessao)
    from database.sqlite.process import ContactsDatabase
    db_instance = ContactsDatabase(sessao_user)
    contatos = db_instance.exibir()
    return contatos


def adicionarcontato(nome, email, endereco, telefone, sessao):
    try:
        if not nome:
            return {'Status': False, 'Message': 'O mínimo para criar um contato é criar o nome'}
        else:
            from SRC.objects.contacts import Contato
            contato = Contato(nome, email, endereco, telefone)
            sessao_user = re.sub(r'[^a-zA-Z]', '', sessao)
            from database.sqlite.process import ContactsDatabase
            print(f'\n\n{sessao_user}')
            db_instance = ContactsDatabase(sessao_user)
            result = db_instance.adicionar(contato)
            if result:
                return {'Status': True, 'Message': 'Cadastro adicionado com sucesso!'}
            else:
                return {'Status': False, 'Message': ''}
    except Exception as error:
        print(f'Erro ao cadastrar novo contato: {error}')
        return {'Status': False, 'Message': ''}


def excluircontato(sessao, id):
    try:
        if not id:
            return {'Status': False, 'Message': 'Problema ao identificar o usuario'}
        else:
            sessao_user = re.sub(r'[^a-zA-Z]', '', sessao)
            from database.sqlite.process import ContactsDatabase
            db_instance = ContactsDatabase(sessao_user)
            result = db_instance.excluir(id)
            if result:
                return {'Status': True, 'Message': 'Contato excluido com sucesso!'}
            else:
                return {'Status': False, 'Message': ''}
    except Exception as error:
        print(f'Erro ao excluir um contato: {error}')
        return {'Status': False, 'Message': ''}
    

def editarcontato(sessao, id, nome, email, endereco, telefone):
    try:
        if not nome:
            return {'Status': False, 'Message': 'O mínimo para criar um contato é definir o nome'}
        else:
            from SRC.objects.contacts import Contato
            contato = Contato(nome, email, endereco, telefone)
            sessao_user = re.sub(r'[^a-zA-Z]', '', sessao)
            from database.sqlite.process import ContactsDatabase
            db_instance = ContactsDatabase(sessao_user)
            result = db_instance.editar(id, contato)
            if result:
                return {'Status': True, 'Message': 'Contato editado com sucesso!'}
            else:
                return {'Status': False, 'Message': ''}
    except Exception as error:
        print(f'Erro ao editar um contato: {error}')
        return {'Status': False, 'Message': ''}


def pesquisarcontato(sessao, dado):
    sessao_user = re.sub(r'[^a-zA-Z]', '', sessao)
    from database.sqlite.process import ContactsDatabase
    db_instance = ContactsDatabase(sessao_user)
    contato = db_instance.pesquisar()
    if contato == False:
        return {'Status': False, 'Message': 'Contato não encontrado'}
    else:
        return contato