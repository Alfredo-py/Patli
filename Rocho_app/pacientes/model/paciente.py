from Rocho_app import db

from decimal import Decimal

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField
from wtforms.validators import InputRequired, NumberRange
class Paciente (db.Model):
    __tablename__="paciente"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255))
    apellidos = db.Column(db.String(255))
    edad = db.Column(db.Integer)
    peso = db.Column(db.Integer)
    talla = db.Column(db.String(255))
    grupo_s = db.Column(db.String(255))
    temperatura = db.Column(db.String(255))
    fecha=db.Column(db.String(255))
    sintomas = db.Column(db.String(255))
    padecimientos = db.Column(db.String(255))
    alergias = db.Column(db.String(255))
    tratamiento = db.Column(db.String(255))
    categoria_id = db.Column(db.Integer, db.ForeignKey('expedientes.id'))
    def __init__(self, nombre,apellidos,edad,peso,talla,grupo_s,temperatura,fecha,sintomas,padecimientos,alergias,tratamiento,categoria_id):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.peso = peso
        self.talla = talla
        self.grupo_s = grupo_s
        self.temperatura = temperatura
        self.fecha = fecha
        self.sintomas = sintomas
        self.padecimientos = padecimientos
        self.alergias = alergias
        self.tratamiento = tratamiento
        self.categoria_id = categoria_id
    def __repr__(self):
        return '<paciente %r>' % (self.nombre)

class PacienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[InputRequired()])
    apellidos = StringField('Apellidos', validators=[InputRequired()])
    edad = DecimalField ('Edad', validators=[InputRequired(), NumberRange(min=Decimal('1'))])
    peso = DecimalField ('Peso', validators=[InputRequired(), NumberRange(min=Decimal('1'))])
    talla = StringField ('Talla',  validators=[InputRequired()])
    grupo_s = StringField('Grupo Sanguineo', validators=[InputRequired()])
    temperatura = StringField('Temperatura', validators=[InputRequired()])
    fecha = StringField('Fecha', validators=[InputRequired()])
    sintomas = StringField('Síntomas', validators=[InputRequired()])
    padecimientos = StringField('Padecimientos', validators=[InputRequired()])
    alergias = StringField('Alergias', validators=[InputRequired()])
    tratamiento = StringField('Tratamiento', validators=[InputRequired()])
    categoria_id = SelectField("Expediente", coerce=int )
    