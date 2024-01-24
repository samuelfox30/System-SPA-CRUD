import re


def exibircontatos(sessao) -> list:
    sessao_user = re.sub(r'[^a-zA-Z]', '', sessao)
    from database.sqlite.process import ContactsDatabase
    db_instance = ContactsDatabase(sessao_user)
    contatos = db_instance.exibir()
    return contatos