from Rocho_app import db

from decimal import Decimal

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import InputRequired, NumberRange
class Categoria (db.Model):
    __tablename__="expedientes"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255))
    pacientes = db.relationship('Paciente',backref= 'categoria', lazy='select')
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __repr__(self):
        return '<Categoria %r>' % (self.nombre)

class CategoriaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[InputRequired()])
    
    