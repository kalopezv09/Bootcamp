from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
listaPersonas = []

db = mysql.connector.connect(
    host="localhost",
    user="root",           
    password="Katha0925",     
    database="sabadoJulio" 
)
cursor = db.cursor(dictionary=True)
#pymysql.cursors.DictCursor para cuando no me sirva mysqal-conne...

#query = "SELECT * FROM persona"
@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'Primera aplicacion web'
    
@app.route('/listarPersonas' ,methods=['GET'])
def listar():
    return jsonify(listaPersonas)


#CODIGO LISTAR
@app.route('/datosDeLaBase',methods=['GET'])
def datosBase():
    #cursor.execute(query)
    cursor.execute("SELECT * FROM persona")
    resultadosPersonas = cursor.fetchall()
    return jsonify(resultadosPersonas)

#CODIGO AGREGAR PERSONAS BASE DE DATOS
@app.route('/AgregarPersonaBD' ,methods=['POST'])
def agregar():
    nuevaPersona = request.json.get('persona')
    listaPersonas.append(nuevaPersona)
    cursor.execute ("INSERT INTO persona(identificacion, nombre, edad) VALUES (%s, %s, %s)",
            (nuevaPersona['identificacion'], nuevaPersona ['nombre'], nuevaPersona ['edad']))
    db.commit()
    return'Se agrego una nueva persona'

#CODIGO PARA BUSCAR
@app.route('/buscarPersona/<identificacion>', methods=['GET'])
def buscar(identificacion):
    cursor.execute("SELECT * FROM persona WHERE identificacion = %s", (identificacion,))
    resultadoPersonas = cursor.fetchall()
    return jsonify(resultadoPersonas)

#CODIGO PARA ACTUALIZAR
@app.route('/actualizarPersona/<identificacion>', methods=['PUT'])
def actualizar(identificacion):
    datos_nuevos = request.json
    cursor.execute("UPDATE persona SET nombre=%s ,edad=%s WHERE identificacion = %s", 
    (datos_nuevos['nombre'], datos_nuevos['edad'], datos_nuevos['identificacion']))
    db.commit()
    return "Persona Actualizada"

#CODIGO PARA ELIMINAR
@app.route('/eliminarPersona/<identificacion>', methods=['DELETE'])
def eliminar(identificacion):
    cursor.execute("DELETE FROM persona WHERE identificacion = %s", 
    (identificacion,))
    db.commit()
    return "Persona Eliminada"

if __name__ == '__main__':
    app.run(debug=True)
