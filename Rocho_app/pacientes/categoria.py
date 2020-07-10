from flask import Blueprint,render_template, request,redirect, url_for, flash, get_flashed_messages

from Rocho_app import db
from Rocho_app.pacientes.model.categoria import Categoria
from flask_login import login_required
from Rocho_app.pacientes.model.categoria import CategoriaForm
expedientes = Blueprint('expedientes',__name__)
@expedientes.before_request
@login_required
def adminitrador():
   print("hecho")
@expedientes.route('/expediente')
@expedientes.route('/expediente/<int:page>')
def home(page=1):
   print()
   return render_template('categoria/index.html',expedientes=Categoria.query.paginate(page,5))

@expedientes.route('/expediente/<int:id>')
def categoria(id):
   categoria = Categoria.query.get_or_404(id)
   return render_template('categoria.html',categoria=categoria)

@expedientes.route('/expediente-delete/<int:id>')
def delete(id):
   expediente = Categoria.query.get_or_404(id)
   print(expediente)
   db.session.delete(expediente) #borrar un registro a la base de datos
   db.session.commit()
   flash("Categoria eliminado con exito")
   return redirect(url_for('expedientes.home'))

@expedientes.route('/expediente-crear',methods=['GET','POST'])
def crear():
   form = CategoriaForm(meta={'csrf':False})
   if form.validate_on_submit():
      p = Categoria(request.form['nombre']) 
      db.session.add(p) #agregar un registro a la base de datos
      db.session.commit() #agregar instruccion para que se pueda subir a la base de datos 
      flash("Categoria creado con exito")
      return redirect(url_for('expedientes.crear'))
   if form.errors:
      flash(form.errors,'danger')

   return render_template('categoria/crear.html',form=form)


@expedientes.route('/expediente-update/<int:id>',methods=['GET','POST'])
def update(id):
   categoria = Categoria.query.get_or_404(id)
   form = CategoriaForm(meta={'csrf':False})
   
   print(categoria.pacientes)
   if request.method == 'GET':
      form.nombre.data=categoria.nombre
   if form.validate_on_submit():
      categoria.nombre = form.nombre.data
      db.session.add(categoria) #agregar un registro a la base de datos
      db.session.commit() #agregar instruccion para que se pueda subir a la base de datos 
      flash("Categoria actualizado con exito")
      return redirect(url_for('expedientes.update',id=categoria.id))
      if form.errors:
         flash(form.errors,'danger')
   return render_template('categoria/update.html',categoria=categoria, form=form)

