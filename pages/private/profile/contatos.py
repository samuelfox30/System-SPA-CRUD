from flask import Flask, Blueprint, render_template, url_for, redirect, request, session

app_contatos = Blueprint('contatos', __name__)


#------------------FUNÇÃO ADICIONAR------------------#
@app_contatos.route('/adicionarcontato', methods=['POST', 'GET'])
def adicionar_contatos():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        endereco = request.form.get('endereco')
        telefone = request.form.get('telefone')
        sessao = session['user']

        from pages.private.profile.contatos_manager import adicionarcontato
        result = adicionarcontato(nome, email, endereco, telefone, sessao)
        if result['Status'] == False:
            mensagem_error = result['Message']
            return render_template('pages/private/profile.html', mensagem_error=mensagem_error)
        elif result['Status'] == True:
            return redirect(url_for('profile.profile'))

    return redirect(url_for('profile.profile'))


#------------------FUNÇÃO EXCLUIR------------------#
@app_contatos.route('/exluir', methods=['POST', 'GET'])
def exluir_contato():
    if request.method == 'POST':
        sessao = session['user']
        id_contato = request.form.get('id')
        print(id_contato)
        from pages.private.profile.contatos_manager import excluircontato
        result = excluircontato(sessao, id_contato)
        if result['Status'] == False:
            mensagem_error = result['Message']
            return render_template('pages/private/profile.html', mensagem_error=mensagem_error)
        elif result['Status'] == True:
            return redirect(url_for('profile.profile'))

    return redirect(url_for('profile.profile'))


#------------------FUNÇÃO EDITAR------------------#
@app_contatos.route('/editar', methods=['POST', 'GET'])
def editar_contato():
    if request.method == 'POST':
        nome = request.form.get('editNome')
        email = request.form.get('editEmail')
        endereco = request.form.get('editEndereco')
        telefone = request.form.get('editTelefone')
        sessao = session['user']
        id_contato = request.form.get('id')
        print(f'\n\n{id_contato}')
        from pages.private.profile.contatos_manager import editarcontato
        result = editarcontato(sessao, id_contato, nome, email, endereco, telefone)
        if result['Status'] == False:
            mensagem_error = result['Message']
            return render_template('pages/private/profile.html', mensagem_error=mensagem_error)
        elif result['Status'] == True:
            return redirect(url_for('profile.profile'))

    return redirect(url_for('profile.profile'))


#------------------FUNÇÃO PESQUISAR------------------#
@app_contatos.route('/pesquisar', methods=['POST', 'GET'])
def pesquisar():
    if request.method == 'POST':
        sessao = session['user']
        dado_de_pesquisa = request.form.get('dado_de_pesquisa')
        from pages.private.profile.contatos_manager import pesquisarcontato
        dado = pesquisarcontato(sessao, dado_de_pesquisa)
        return render_template('pages/private/profile.html', contatos=dado)
    else:
        return redirect(url_for('profile.profile'))