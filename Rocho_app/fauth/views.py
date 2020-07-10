from flask import Blueprint,session,render_template, request,redirect, url_for, flash, get_flashed_messages, abort
from Rocho_app.auth.model.user import Usuario, LoginForm,RegisterForm
from Rocho_app import db
from Rocho_app import administrador
from flask_login import login_user, logout_user, current_user, login_required
from Rocho_app import login_manager
fauth = Blueprint('fauth',__name__)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

@fauth.route('/registro',methods=['GET','POST'])
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
        return redirect(url_for('fauth.registro'))
    if form.errors:
        flash(form.errors,'danger')

    return render_template('auth/registro.html',form=form)


@fauth.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash("Ya estas autenticado")
        return redirect(url_for("expedientes.home"))
    form = LoginForm(meta={'csrf':False})
    
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Bienvenido "+ user.username+" 😀")
            next = request.form['next'] 
            print(next)
            return redirect(next or url_for('expedientes.home'))
        else:
            flash("Ingreso su usuario y/o contraseña mal",'danger')
        return redirect(url_for('fauth.login'))
    if form.errors:
        flash(form.errors,'danger')

    return render_template('auth/login.html',form=form)
@fauth.route('/logout',methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('fauth.login'))

@fauth.route("/protegido")
@login_required
def protegido():
    return "vista protegida"