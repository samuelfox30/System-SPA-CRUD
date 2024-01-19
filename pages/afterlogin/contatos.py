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
            print(f'Dados recebidos:\nNome: {nome}\Email: {email}\nEndereco: {endereco}\nTelefone: {telefone}')
        except Exception as error:
            print(f'Erro ao receber dados do formulario: {error}')
    else:
        return redirect(url_for('profile'))
    
    
@app_contatos.route('/editar')
def logout():
    pass