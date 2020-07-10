from Rocho_app import db


from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField ,HiddenField
from wtforms.validators import InputRequired,EqualTo
from sqlalchemy import Enum
from werkzeug.security import check_password_hash,generate_password_hash
import enum

class Rol(enum.Enum):
    medico='medico'
    admin='admin'

class Usuario (db.Model):
    __tablename__="usuarios"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(300))
    rol = db.Column(Enum(Rol))

    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)

    def __init__(self, username, password,rol=Rol.medico):
        self.username = username
        self.password = generate_password_hash(password)
        self.rol = rol
    def __repr__(self):
        return '<User %r>' % (self.nombre)

    def check_password(self,password):
        return check_password_hash(self.password,password)

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired()])
    next = HiddenField('next')
class RegisterForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired(),EqualTo('confirmar')])
    confirmar = PasswordField('Repetir Contraseña')

class ChangePassword(FlaskForm):
    password = PasswordField('Nueva Contraseña', validators=[InputRequired(),EqualTo('confirm',message="La contraseña debe coincidir")])
    confirmar = PasswordField('Repetir Contraseña')
