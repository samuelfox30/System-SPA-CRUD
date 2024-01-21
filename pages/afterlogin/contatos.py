from flask import Flask, Blueprint, render_template, url_for, redirect, request, session

app_contatos = Blueprint('contatos', __name__)

#------------------FUNÇÃO PRINCIPAL------------------#
@app_contatos.route('/adicionar', methods=['POST', 'GET'])
def contatos():
    if request.method == 'POST':
        try:
            nome = request.form.get('nome')
            email = request.form.get('email')
            endereco = request.form.get('endereco')
            telefone = request.form.get('telefone')
            if not nome:
                mensagem_minimo_nome = 'O mínimo para criar um contato é criar o nome'
                return render_template('pages/afterlogin/profile.html', mensagem_error=mensagem_minimo_nome)
            else:
                usuario = session['user']
                print(f'\n\nUsuario: {usuario}')
                from backend.system.afterlogin.objects import Contato
                contato = Contato(nome, email, endereco, telefone)
                from backend.database.afterlogin.databasemanager.process import SystemDatabase
                db_instance = SystemDatabase(usuario)
                db_instance.cadastrar(contato)
        except Exception as error:
            print(f'Erro ao receber dados do formulario: {error}')
    
    return redirect(url_for('profile.profile'))
    
    
@app_contatos.route('/editar')
def logout():
    return 'teste'