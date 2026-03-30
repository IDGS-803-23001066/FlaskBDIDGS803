from . import maestros_bp
from flask import Blueprint, redirect, render_template, request, url_for
from models import Maestros, db
from forms import MaestroForm




@maestros_bp.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"


@maestros_bp.route("/Maestros", methods=['GET','POST'])
def lista_maestros():

    create_form = MaestroForm(request.form)
    maestros = Maestros.query.all()

    if request.method == 'POST' and create_form.validate():

        maestro = Maestros(
            matricula=create_form.matricula.data,
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )

        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for('maestros.lista_maestros'))

    return render_template(
        "listadoMaestros.html",
        form=create_form,
        maestros=maestros
    )


@maestros_bp.route("/detalles_maestro")
def detalles_maestro():

    matricula = request.args.get('matricula')
    maestro = Maestros.query.get(matricula)

    return render_template(
        "detallesMaestros.html",
        nombre=maestro.nombre,
        apellidos=maestro.apellidos,
        especialidad=maestro.especialidad,
        email=maestro.email
    )


@maestros_bp.route("/modificar_maestro", methods=['GET','POST'])
def modificar_maestro():

    create_form = MaestroForm(request.form)

    if request.method == 'GET':
        matricula = request.args.get('matricula')
        maestro = Maestros.query.get(matricula)

        create_form.matricula.data = maestro.matricula
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email

    if request.method == 'POST' and create_form.validate():
        matricula = create_form.matricula.data
        maestro = Maestros.query.get(matricula)

        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.especialidad = create_form.especialidad.data
        maestro.email = create_form.email.data

        db.session.commit()

        return redirect(url_for('maestros.lista_maestros'))

    return render_template("modificarMaestros.html", form=create_form)


@maestros_bp.route("/eliminar_maestro", methods=['GET','POST'])
def eliminar_maestro():

    create_form = MaestroForm(request.form)

    if request.method == 'GET':
        matricula = request.args.get('matricula')
        maestro = Maestros.query.get(matricula)

        create_form.matricula.data = maestro.matricula
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email

    if request.method == 'POST':
        matricula = create_form.matricula.data
        maestro = Maestros.query.get(matricula)

        db.session.delete(maestro)
        db.session.commit()

        return redirect(url_for('maestros.lista_maestros'))

    return render_template("eliminarMaestros.html", form=create_form)


@maestros_bp.route("/registrar_maestro", methods=['GET','POST'])
def registrar_maestro():

    create_form = MaestroForm(request.form)

    if request.method == 'POST' and create_form.validate():

        maestro_existente = Maestros.query.filter_by(
            matricula=create_form.matricula.data
        ).first()

        if maestro_existente:
            return "Ya existe un maestro con esa matrícula"

        maestro = Maestros(
            matricula=create_form.matricula.data,
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )

        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for('maestros.lista_maestros'))

    return render_template("Maestros.html", form=create_form)