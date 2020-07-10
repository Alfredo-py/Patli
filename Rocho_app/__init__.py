from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, logout_user
from functools import wraps
app = Flask(__name__)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#app.config['SQLALCHEMY_DATABASE_URI']=
app.config.from_object('configuration.DevelopmentConfig')
app.config['DOWNLOAD_FOLDER'] = '../recetas'
descargas=app.config['DOWNLOAD_FOLDER']
db=SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "fauth.login"
def administrador(f):
    @wraps(f)
    def wrapper(*args,**kwds):
        print(current_user.rol.value)
        if current_user.rol.value != "admin":
            logout_user()
            return redirect(url_for('fauth.login'))
            #login_manager.unauthorized()
            #return "Tu debes de ser Administrador",403
        return f(*args,**kwds)
    return wrapper
from Rocho_app.pacientes.paciente import pacientes
from Rocho_app.pacientes.categoria import expedientes
from Rocho_app.auth.views import auth
from Rocho_app.fauth.views import fauth

app.register_blueprint(pacientes)
app.register_blueprint(expedientes)
#app.register_blueprint(auth)
app.register_blueprint(fauth)

db.create_all()
