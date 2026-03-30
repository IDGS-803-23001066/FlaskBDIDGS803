from . import consultas_bp
from flask import render_template, request
from models import Curso, Alumnos



@consultas_bp.route("/alumnos_por_curso", methods=['GET','POST'])
def alumnos_por_curso():

    cursos = Curso.query.all()
    alumnos = []
    curso_seleccionado = None

    if request.method == 'POST':

        curso_id = int(request.form.get('curso_id'))
        curso_seleccionado = Curso.query.get(curso_id)

        if curso_seleccionado:
            alumnos = curso_seleccionado.alumnos

    return render_template(
        "alumnosCurso.html",
        cursos=cursos,
        alumnos=alumnos,
        curso=curso_seleccionado
    )



@consultas_bp.route("/cursos_por_alumno", methods=['GET','POST'])
def cursos_por_alumno():

    alumnos = Alumnos.query.all()
    cursos = []
    alumno_seleccionado = None

    if request.method == 'POST':

        alumno_id = int(request.form.get('alumno_id'))
        alumno_seleccionado = Alumnos.query.get(alumno_id)

        if alumno_seleccionado:
            cursos = alumno_seleccionado.cursos

    return render_template(
        "cursosAlumno.html",
        alumnos=alumnos,
        cursos=cursos,
        alumno=alumno_seleccionado
    )