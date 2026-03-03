from wtforms import Form, IntegerField, StringField
from wtforms import validators

class UserForm(Form):

    id = IntegerField('id')

    nombre = StringField('nombre', [
        validators.DataRequired(),
        validators.Length(min=4, max=20)
    ])

    apellidos = StringField('apellidos', [
        validators.DataRequired(),
        validators.Length(min=4, max=50)
    ])

    email = StringField('email', [
        validators.DataRequired(),
        validators.Length(min=4, max=50)
    ])

    telefono = StringField('telefono', [
        validators.DataRequired(),
        validators.Length(min=10, max=15)
    ])

class MaestroForm(Form):

      matricula = IntegerField('matricula', [
        validators.DataRequired()
    ])

      nombre = StringField('nombre', [
        validators.DataRequired(),
        validators.Length(min=4, max=50)
    ])

      apellidos = StringField('apellidos', [
        validators.DataRequired(),
        validators.Length(min=4, max=50)
    ])

      especialidad = StringField('especialidad', [
        validators.DataRequired(),
        validators.Length(min=4, max=50)
    ])

      email = StringField('email', [
        validators.DataRequired(),
        validators.Length(min=4, max=50)
    ])