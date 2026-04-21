from flask import Blueprint, render_template, jsonify
from modules.database import leer_datos, guardar_datos

checklist_bp = Blueprint('checklist', __name__)

@checklist_bp.route('/')
def inicio():
    datos = leer_datos()
    return render_template('checklist/index.html', tareas=datos['tasks'])

@checklist_bp.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    datos = leer_datos()
    for tarea in datos['tasks']:
        if tarea['id'] == id:
            tarea['hecho'] = not tarea['hecho']
    guardar_datos(datos)
    return jsonify({'ok': True})