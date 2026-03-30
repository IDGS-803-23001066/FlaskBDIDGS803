from . import inscripciones_bp
from flask import redirect, render_template, request, url_for
from models import Alumnos, Curso, db
from forms import InscripcionForm


@inscripciones_bp.route("/Inscripciones", methods=['GET','POST'])
def lista_inscripciones():

    create_form = InscripcionForm(request.form)


    alumnos = Alumnos.query.all()
    cursos = Curso.query.all()

    create_form.alumno_id.choices = [(a.id, a.nombre) for a in alumnos]
    create_form.curso_id.choices = [(c.id, c.nombre) for c in cursos]

    if request.method == 'POST' and create_form.validate():

        alumno = Alumnos.query.get(create_form.alumno_id.data)
        curso = Curso.query.get(create_form.curso_id.data)

        
        curso.alumnos.append(alumno)

        db.session.commit()

        return redirect(url_for('inscripciones.lista_inscripciones'))

    return render_template(
        "inscripciones.html",
        form=create_form
    )