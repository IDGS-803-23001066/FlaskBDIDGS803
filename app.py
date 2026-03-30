from flask import Flask, render_template
from config import DevelopmentConfig
from models import db
from flask_wtf.csrf import CSRFProtect

from alumnos import alumnos_bp
from maestros.routes import maestros_bp
from cursos.routes import cursos_bp
from inscripciones.routes import inscripciones_bp
from consultas import consultas_bp

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)


csrf = CSRFProtect(app)


app.register_blueprint(alumnos_bp)
app.register_blueprint(maestros_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(inscripciones_bp)
app.register_blueprint(consultas_bp)


@app.route('/')
def bienvenida():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)