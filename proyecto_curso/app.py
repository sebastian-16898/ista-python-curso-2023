from flask import Flask, jsonify,request
from datos import datos
app = Flask(__name__)


@app.route('/')
def alumno():
    a=datos("Python","0107291452")
    b=datos("Java","0107291452")
    a.imprimir()
    b.imprimir()
    return 'PROYECTO FINAL'

@app.route('/get_alumno')
def extraer_datos():
    try:
        return datos.leer_archivo()
    except Exception:
        return "Error"
    
@app.route('/get_asistencia')
def extraer_asistencia():
    try:
        return datos.leer_asistencia()
    except Exception:
        return "Error"
    
@app.route('/post_asistencia/<cedula>/<nombre_materia>/<ano>/<mes>/<hora>')
def escribir(cedula, nombre_materia, ano, mes , hora):
    try:
        datos.escrbir_datos(cedula, nombre_materia, ano, mes , hora)
        asistencia=datos.leer_asistencia()
        return asistencia
    except Exception:
        return "error"

@app.route('/busca_asistencia/<cedula>/<curso>')
def buscar_asistencia(cedula, curso):
    try:
        return datos.buscar_asistencia(cedula,curso)        
    except Exception:
        return "error"
    