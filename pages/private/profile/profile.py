from flask import Flask, Blueprint, render_template, url_for, redirect, request, session

app_profile = Blueprint('profile', __name__)

#------------------FUNÇÃO PRINCIPAL------------------#
@app_profile.route('/profile')
def profile():
    if 'user' in session:
        usuario = session['user']
        # Carregar dados e passar para o html
        return render_template('pages/afterlogin/profile.html')
    else:
        return redirect(url_for('index.index'))
    
    
@app_profile.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index.index'))