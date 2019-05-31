from flask import Flask

app = Flask(__name__)

@app.route("/usuario/<nome>")
def hello_world(nome):
    return ("Olá %s! Estou aprendendo Flask"%(nome), 200)

@app.route("/noticias/<categoria>")
def getNoticias(Categoria):
    pass

@app.route("/usuario/<int:id>", methods=['GET'])
def getUsuario(id):
    usuarios = [{1: "João"}, {2: "Maria"}, {3: "José"}]
    for usuario in usuarios:
        if (id in usuario.keys()):
            print(usuario[id])
            return(usuario[id], 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
