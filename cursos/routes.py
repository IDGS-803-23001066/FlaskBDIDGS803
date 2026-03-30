from . import cursos_bp
from flask import redirect, render_template, request, url_for
from models import Curso, Maestros, db
from forms import CursoForm



@cursos_bp.route("/Cursos", methods=['GET','POST'])
def lista_cursos():

    create_form = CursoForm(request.form)

    
    create_form.maestro_id.choices = [
        (m.matricula, m.nombre) for m in Maestros.query.all()
    ]

    cursos = Curso.query.all()

    if request.method == 'POST' and create_form.validate():

        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )

        db.session.add(curso)
        db.session.commit()

        return redirect(url_for('cursos.lista_cursos'))

    return render_template(
        "listadoCursos.html",
        form=create_form,
        cursos=cursos
    )


@cursos_bp.route("/detalles_curso")
def detalles_curso():

    id = int(request.args.get('id'))
    curso = Curso.query.get(id)

    if not curso:
        return redirect(url_for('cursos.lista_cursos'))

    return render_template(
        "detallesCursos.html",
        nombre=curso.nombre,
        descripcion=curso.descripcion,
        maestro=curso.maestro.nombre
    )


@cursos_bp.route("/modificar_curso", methods=['GET','POST'])
def modificar_curso():

    create_form = CursoForm(request.form)

    create_form.maestro_id.choices = [
        (m.matricula, m.nombre) for m in Maestros.query.all()
    ]

    if request.method == 'GET':

        id = int(request.args.get('id'))
        curso = Curso.query.get(id)

        if not curso:
            return redirect(url_for('cursos.lista_cursos'))

        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id


    if request.method == 'POST' and create_form.validate():

        id = create_form.id.data
        curso = Curso.query.get(id)

        curso.nombre = create_form.nombre.data
        curso.descripcion = create_form.descripcion.data
        curso.maestro_id = create_form.maestro_id.data

        db.session.commit()

        return redirect(url_for('cursos.lista_cursos'))


    return render_template(
        "modificarCursos.html",
        form=create_form
    )



@cursos_bp.route("/eliminar_curso", methods=['GET','POST'])
def eliminar_curso():
    create_form = CursoForm(request.form)

    if request.method == 'POST':
       
        id = create_form.id.data
        curso = Curso.query.get(id)

        if curso:
            db.session.delete(curso)
            db.session.commit()

        return redirect(url_for('cursos.lista_cursos'))

 
    id = request.args.get('id', type=int)
    curso = Curso.query.get(id)

    if not curso:
        return redirect(url_for('cursos.lista_cursos'))

    
    create_form.id.data = curso.id
    create_form.nombre.data = curso.nombre
    create_form.descripcion.data = curso.descripcion
    create_form.maestro_id.data = curso.maestro_id

    return render_template(
        "eliminarCursos.html",
        form=create_form
    )


@cursos_bp.route("/registrar_curso", methods=['GET','POST'])
def registrar_curso():

    create_form = CursoForm(request.form)

    create_form.maestro_id.choices = [
        (m.matricula, m.nombre) for m in Maestros.query.all()
    ]

    if request.method == 'POST' and create_form.validate():

        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )

        db.session.add(curso)
        db.session.commit()

        return redirect(url_for('cursos.lista_cursos'))

    return render_template(
        "Cursos.html",
        form=create_form
    )