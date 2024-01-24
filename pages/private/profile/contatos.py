from flask import Flask, Blueprint, render_template, url_for, redirect, request, session

app_contatos = Blueprint('contatos', __name__)

#------------------FUNÇÃO PRINCIPAL------------------#
@app_contatos.route('/adicionarcontato', methods=['POST', 'GET'])
def adicionar_contatos():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        endereco = request.form.get('endereco')
        telefone = request.form.get('telefone')
        sessao = session['user']
        
        # Carregando dados para tabela
        from pages.private.profile.profile_manager import exibircontatos
        contatos = exibircontatos(sessao)

        from pages.private.profile.contatos_manager import adicionarcontato
        result = adicionarcontato(nome, email, endereco, telefone, sessao)
        if result['Status'] == False:
            mensagem_error = result['Message']
            return render_template('pages/private/profile.html', contatos=contatos, mensagem_error=mensagem_error)
        elif result['Status'] == True:
            mensagem_success = result['Message']
            return render_template('pages/private/profile.html', contatos=contatos, mensagem_success=mensagem_success)

    
    return redirect(url_for('profile.profile'))
    
    
@app_contatos.route('/editar')
def logout():
    return 'teste'