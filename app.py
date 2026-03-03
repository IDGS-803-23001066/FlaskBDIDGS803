from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask import g
from maestros.routes import maestros
from forms import MaestroForm
from models import Maestros

import forms
from models import db
from models import Alumnos
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()

@app.route("/",methods=['GET','POST'])
@app.route("/index")
def index():
	create_form=forms.UserForm(request.form)
	alumno=Alumnos.query.all()
	return render_template("index.html",form=create_form,alumno=alumno)

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    create_form = forms.UserForm(request.form)

    if request.method == 'POST' and create_form.validate():

        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )

        db.session.add(alum)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template("Alumnos.html", form=create_form)

@app.route("/detalles")
def detalles():

    id = request.args.get('id')
    alum = Alumnos.query.get(id)

    return render_template(
        "detalles.html",
        nombre=alum.nombre,
        apellidos=alum.apellidos,
        email=alum.email,
        telefono=alum.telefono
    )

@app.route("/modificar", methods=['GET','POST'])
def modificar():

    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum = Alumnos.query.get(id)

        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.email.data = alum.email
        create_form.telefono.data = alum.telefono

    if request.method == 'POST' and create_form.validate():
        id = create_form.id.data
        alum = Alumnos.query.get(id)

        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        alum.telefono = create_form.telefono.data

        db.session.commit()

        return redirect(url_for('index'))

    return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=['GET','POST'])
def eliminar():

    create_form = forms.UserForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum = Alumnos.query.get(id)

        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apellidos.data = alum.apellidos
        create_form.email.data = alum.email
        create_form.telefono.data = alum.telefono

    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)

        db.session.delete(alum)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template("eliminar.html", form=create_form)




@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

if __name__ == '__main__':
	csrf.init_app(app)
	
	with app.app_context():
		db.create_all()
	app.run(debug=True)
