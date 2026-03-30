from . import alumnos_bp
from flask import render_template, request, redirect, url_for
from models import db, Alumnos
import forms


@alumnos_bp.route("/alumnos")
def listado():

    alumnos = Alumnos.query.all()

    return render_template(
        "listado.html",
        alumnos=alumnos
    )


@alumnos_bp.route("/nuevo", methods=['GET','POST'])
def agregar():

    create_form = forms.UserForm(request.form)

    if request.method == 'POST' and create_form.validate():

        alumno_existente = Alumnos.query.filter_by(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data
        ).first()

        if alumno_existente:
            return "El alumno ya existe"

        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            email=create_form.email.data
        )

        db.session.add(alum)
        db.session.commit()

        return redirect(url_for('alumnos_bp.listado'))

    return render_template(
        "agregar.html",
        form=create_form
    )


@alumnos_bp.route("/detalles")
def detalles():

    id = request.args.get('id')
    alum = Alumnos.query.get(id)

    return render_template(
        "detalles.html",
        id=alum.id,
        nombre=alum.nombre,
        apellidos=alum.apaterno,
        email=alum.email
    )


@alumnos_bp.route("/modificar", methods=['GET','POST'])
def modificar():

    create_form = forms.UserForm(request.form)

    if request.method == 'GET':

        id = request.args.get('id')
        alum = Alumnos.query.get(id)

        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apaterno.data = alum.apaterno
        create_form.email.data = alum.email

    if request.method == 'POST' and create_form.validate():

        id = create_form.id.data
        alum = Alumnos.query.get(id)

        alum.nombre = create_form.nombre.data
        alum.apaterno = create_form.apaterno.data
        alum.email = create_form.email.data

        db.session.commit()

        return redirect(url_for('alumnos_bp.listado'))

    return render_template("modificar.html", form=create_form)



@alumnos_bp.route("/eliminar", methods=['GET','POST'])
def eliminar():

    create_form = forms.UserForm(request.form)

    if request.method == 'GET':

        id = request.args.get('id')
        alum = Alumnos.query.get(id)

        create_form.id.data = alum.id
        create_form.nombre.data = alum.nombre
        create_form.apaterno.data = alum.apaterno
        create_form.email.data = alum.email

    if request.method == 'POST':

        id = create_form.id.data
        alum = Alumnos.query.get(id)

        db.session.delete(alum)
        db.session.commit()

        return redirect(url_for('alumnos_bp.listado'))

    return render_template(
        "eliminar.html",
        form=create_form
    )