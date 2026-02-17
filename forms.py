from wtforms import Form, IntegerField, StringField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id')

    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.Length(min=4, max=20, message='required min=4 max=20')
    ])

    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El apellido paterno es requerido'),
        validators.Length(min=4, max=20, message='required min=4 max=20')
    ])

    amaterno = StringField('amaterno', [
        validators.DataRequired(message='El apellido materno es requerido'),
        validators.Length(min=4, max=20, message='required min=4 max=20')
    ])

    email = StringField('email', [
        validators.DataRequired(message='El email es requerido'),
        validators.Length(min=4, max=50, message='required min=4 max=50')
    ])
