from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
listaPersonas = []

@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'Primera aplicacion web'
    
@app.route('/listarPersonas' ,methods=['GET'])
def listar():
    return jsonify(listaPersonas)

@app.route('/AgregarPersona' ,methods=['POST'])
def agregar():
    nuevaPersona = request.json.get('persona')
    listaPersonas.append(nuevaPersona)
    return'Se agrego una nueva persona'

if __name__ == '__main__':
    app.run(debug=True)
