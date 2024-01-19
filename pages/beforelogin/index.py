from flask import Flask, Blueprint, render_template, url_for, redirect, request, session

app_index = Blueprint('index', __name__)

#------------------FUNÇÃO PRINCIPAL------------------#
@app_index.route('/')
def index():
    """ from backend.database.beforelogin.databasesmanager.process import SystemDatabase
    db_intance = SystemDatabase()
    db_intance.excluir_manual('samuelfoxgama@hotmail.com') """
    if 'user' in session:
        return redirect(url_for('profile.profile'))
    return render_template('pages/beforelogin/index.html')


#------------------FUNÇÃO CADASTRAR------------------#
@app_index.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():

    if request.method == 'POST':
        try:
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')

            if not nome or not email or not senha:
                pass
            else:
                from backend.system.beforelogin.settings import verificar_senha
                mensagem_senha = verificar_senha(senha)
                if mensagem_senha is None:

                    # ---------------- Se tudo der certo: ---------------- #
                    from backend.system.beforelogin.objects import UserCadastro
                    Usuario_para_cadastro = UserCadastro(nome, email, senha)
                    from backend.database.beforelogin.databasesmanager.process import SystemDatabase
                    db_intance = SystemDatabase()
                    if db_intance.verificar_existencia(Usuario_para_cadastro):                        
                        db_intance.cadastrar(Usuario_para_cadastro)
                    else:
                        mensagem_ja_cadastrado_anteriormente = 'Seu email ja está cadastrado em nossa plataforma!'
                        return render_template('pages/beforelogin/index.html', mensagem=mensagem_ja_cadastrado_anteriormente)

                else:
                    return render_template('pages/beforelogin/index.html', mensagem=mensagem_senha)

        except Exception as error:
            print(f'Algo deu errado ao cadastrar o usuario: {error}')

    # Redireciona para a rota principal após o cadastro
    return redirect(url_for('index.index'))


#------------------FUNÇÃO LOGAR------------------#
@app_index.route('/logar', methods=['POST', 'GET'])
def logar():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            senha = request.form.get('senha')

            if not email or not senha:
                pass
            else:

                # ---------------- Se tudo der certo: ---------------- #
                from backend.system.beforelogin.objects import UserLogin
                Usuario_para_login = UserLogin(email, senha)
                from backend.database.beforelogin.databasesmanager.process import SystemDatabase
                db_intance = SystemDatabase()
                if db_intance.verificar_existencia(Usuario_para_login):
                    mensagem_nao_cadastrado = 'Seu email não está cadastrado em nossa plataforma!'
                    return render_template('pages/beforelogin/index.html', mensagem=mensagem_nao_cadastrado)
                else:
                    if db_intance.permitir_login(Usuario_para_login):
                        session['user'] = email
                        return redirect(url_for('profile.profile'))
                        pass
                    else:
                        mensagem_login_nao_permitido = 'Email ou senha incorreta!'
                        return render_template('pages/beforelogin/index.html', mensagem=mensagem_login_nao_permitido)
                

        except Exception as error:
            print(f'Algo deu errado ao cadastrar o usuario: {error}')

    # Redireciona para a rota principal após o login
    return redirect(url_for('index.index'))
