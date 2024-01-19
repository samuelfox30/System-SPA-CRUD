from flask import Flask, Blueprint, url_for

# Import Páginas
from pages.beforelogin.index import app_index
from pages.afterlogin.profile import app_profile

app = Flask(__name__)
app.secret_key = 'minhasecretkeyemuitodificil'

# Add Páginas
app.register_blueprint(app_index)
app.register_blueprint(app_profile)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')