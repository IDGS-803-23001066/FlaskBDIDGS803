from wtforms import Form, IntegerField, StringField, TextAreaField, SelectField
from wtforms import validators



class UserForm(Form):

    id = IntegerField('ID')

    nombre = StringField('Nombre', [
        validators.DataRequired(),
        validators.Length(min=2, max=50)
    ])

    apaterno = StringField('Apellido', [
        validators.DataRequired(),
        validators.Length(min=2, max=50)
    ])

    email = StringField('Email', [
        validators.DataRequired(),
        validators.Email()
    ])



class MaestroForm(Form):

    matricula = IntegerField('Matricula', [
        validators.DataRequired()
    ])

    nombre = StringField('Nombre', [
        validators.DataRequired(),
        validators.Length(min=2, max=50)
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired(),
        validators.Length(min=2, max=50)
    ])

    especialidad = StringField('Especialidad', [
        validators.DataRequired(),
        validators.Length(min=2, max=50)
    ])

    email = StringField('Email', [
        validators.DataRequired(),
        validators.Email()
    ])


class CursoForm(Form):

    id = IntegerField('ID')

    nombre = StringField('Nombre del Curso', [
        validators.DataRequired(),
        validators.Length(min=3, max=150)
    ])

    descripcion = TextAreaField('Descripcion', [
        validators.Optional(),
        validators.Length(max=500)
    ])

    maestro_id = SelectField(
        'Maestro',
        coerce=int
    )



class InscripcionForm(Form):

    alumno_id = SelectField(
        'Alumno',
        coerce=int
    )

    curso_id = SelectField(
        'Curso',
        coerce=int
    )