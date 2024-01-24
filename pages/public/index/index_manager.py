def Cadastrar(nome, email, senha):
    try:
        if not nome or not email or not senha:
           return {'Status': False, 'Message': 'Dados faltando'}
        else:
            from SRC.system.standars import check_standar_email
            if check_standar_email(email):
                from SRC.system.standars import check_standar_senha
                result_senha_check = check_standar_senha(senha)
                if result_senha_check is None:
                    from SRC.objects.users import UserCadastro
                    user = UserCadastro(nome, email, senha)
                    from database.sqlite.process import SystemDatabase
                    db_instance = SystemDatabase()
                    if db_instance.verificar_existencia(user):
                        return {'Status': False, 'Message': 'Seu email ja está cadastrado no sistema'}
                    else:
                        # Se tudo der certo
                        if db_instance.cadastrar(user):
                            return {'Status': True, 'Message': 'Cadastro realizado com exito!'}
                        else:
                            return {'Status': False}
                else:
                    return {'Status': False, 'Message': result_senha_check}
            else:
                return {'Status': False, 'Message': 'Email no formato não valido'}
            
    except Exception as error:
        print(f'\nErro ao realizar o cadastro, Arquivo: index_manager.py, Erro: {error}')
        return {'Status': False}


def Logar(email, senha):
    try:
        if not email or not senha:
           return {'Status': False, 'Message': 'Dados faltando'}
        else:
            from SRC.objects.users import UserLogin
            user = UserLogin(email, senha)
            from database.sqlite.process import SystemDatabase
            db_instance = SystemDatabase()
            if db_instance.verificar_existencia(user):
                if db_instance.permitir_login(user):
                    # Se tudo der certo
                    return {'Status': True}
                else:
                    return {'Status': False, 'Message': 'Senha incorreta'}
            else:
                return {'Status': False, 'Message': 'Seu email não está cadastrado no sistema'}

    except Exception as error:
        print(f'\nErro ao realizar o cadastro, Arquivo: index_manager.py, Erro: {error}')
        return {'Status': False}