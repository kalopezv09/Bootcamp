from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
DatosInnoweb = []
numero_actual = 1

@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'Primera aplicacion web'
    
@app.route('/ListarDatosInnoweb' ,methods=['GET'])
def listar():
    return jsonify(DatosInnoweb )

@app.route('/IngresarDatosInnoweb' ,methods=['POST'])
def agregar():
    nuevoUsuario = request.json.get('Usuario')
    DatosInnoweb.append(nuevoUsuario)
    return'Se agrego una nueva persona'

@app.route('/eliminarPersona/<int:numero>', methods=['DELETE'])
def eliminar(numero):
    idx = numero - 1
    if 0 <= idx < len(DatosInnoweb):
        eliminado = DatosInnoweb.pop(idx)
        return jsonify({
            'mensaje': f'Usuario {eliminado["Nombre"]} eliminado correctamente'
        }), 200
    else:
        return jsonify({
            'error': f'Número {numero} fuera de rango'
             }), 404


if __name__ == '__main__':
    app.run(debug=True)
