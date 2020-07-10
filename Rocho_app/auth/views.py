from flask import Blueprint,session,render_template, request,redirect, url_for, flash, get_flashed_messages
from Rocho_app.auth.model.user import Usuario, LoginForm,RegisterForm
from Rocho_app import db

auth = Blueprint('auth',__name__)

@auth.route('/registro',methods=['GET','POST'])
def registro():
    form = RegisterForm(meta={'csrf':False})
    if form.validate_on_submit():
        if Usuario.query.filter_by(username=form.username.data).first():
            flash("Ya existe este usuario en el sistema",'danger')
        else:
            p = Usuario(form.username.data,form.password.data) 
            db.session.add(p) #agregar un registro a la base de datos
            db.session.commit() #agregar instruccion para que se pueda subir a la base de datos 
            flash("Usuario creado con exito")
        return redirect(url_for('auth.registro'))
    if form.errors:
        flash(form.errors,'danger')

    return render_template('auth/registro.html',form=form)


@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm(meta={'csrf':False})
    if 'username' not in session:
        if form.validate_on_submit():
            user = Usuario.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                session['username'] = user.username
                session['rol'] = user.rol.value
                session['id'] = user.id
                flash("Bienvenido "+ user.username)
                return redirect(url_for('expedientes.home'))
            else:
                flash("Ingreso su usuario y/o contraseña mal",'danger')
            return redirect(url_for('auth.registro'))
    if form.errors:
        flash(form.errors,'danger')

    return render_template('auth/login.html',form=form)
@auth.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('username')
    session.pop('rol')
    session.pop('id')
    return redirect(url_for('auth.login'))