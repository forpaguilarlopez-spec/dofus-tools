from flask import Blueprint, render_template, jsonify
import json

checklist_bp = Blueprint('checklist', __name__)

DATA_FILE = 'data.json'

def leer_datos():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_datos(datos):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

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