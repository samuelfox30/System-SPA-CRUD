from flask import Flask, Blueprint, render_template, url_for, redirect, request, session

app_index = Blueprint('index', __name__)

#------------------FUNÇÃO PRINCIPAL------------------#
@app_index.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('profile.profile'))
    return render_template('pages/public/index.html')


#------------------FUNÇÃO CADASTRAR------------------#
@app_index.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        from pages.public.index.index_manager import Cadastrar
        result = Cadastrar(nome, email, senha)
        if result['Status'] == False:
            mensagem_error = result['Message']
            return render_template('pages/public/index.html', mensagem_error=mensagem_error)
        elif result['Status'] == True:
            mensagem_success = result['Message']
            return render_template('pages/public/index.html', mensagem_success=mensagem_success)

    return redirect(url_for('index.index'))


#------------------FUNÇÃO LOGAR------------------#
@app_index.route('/logar', methods=['POST', 'GET'])
def logar():

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        from pages.public.index.index_manager import Logar
        result = Logar(email, senha)
        if result['Status'] == False:
            mensagem_error = result['Message']
            return render_template('pages/public/index.html', mensagem_error=mensagem_error)
        elif result['Status'] == True:
            session['user'] = email
            return redirect(url_for('profile.profile'))
        
    return redirect(url_for('index.index'))
