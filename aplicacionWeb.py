from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'Primera aplicacion web'
    
@app.route('/listarPersonas' ,methods=['GET'])
def listar():
    listarPersonas = ['Andrea','Jeferson','Mordelon']
    return jsonify(listarPersonas)

@app.route('/DatosPersonas' ,methods=['GET'])
def Datos():
    DatosPersonas = [{"Nombre":"Andrea", "Edad":28 , "Profesion":"Ingeniera Civil"},
                     {"Nombre":"Jeferson", "Edad":29 , "Profesion":"Programador y Comunicador Social"},
                     {"Nombre":"Mordelon", "Edad":13 , "Profesion":"Perrito"}]
    return jsonify(DatosPersonas)

#ejercicio 2 ejemplos relacionado a nuestro proyecto

@app.route('/Innoweb' ,methods=['GET'])
def Innoweb():
    Innoweb = ['Usuario','Proyecto','Tarea','Comentario']
    return jsonify(Innoweb) 

@app.route('/DatosItems' ,methods=['GET'])
def Items():
    DatosItems = ['Usuario',
                  {"Nombre":"Jesus", "Email":"Jesus@innoweb.com" , "Rol":"Programador Junior"},
                  {"Nombre":"Maria", "Email":"maria@innoweb.com" , "Profesion":"Programador"},
                  {"Nombre":"Jose", "Email":"jose@innoweb.com" , "Profesion":"Asistente"},
                  'Proyecto',
                  {"Nombre":"Avacakes", "Descripcion":"Pagina ecoomerce Pasteleria Saludable","Fecha Inicio":"Enero 12","Fecha Fin":"Diciembre 15"}]
                
    return jsonify(DatosItems)

if __name__ == '__main__':
    app.run(debug=True)
