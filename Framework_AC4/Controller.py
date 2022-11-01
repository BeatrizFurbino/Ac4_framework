from flask import Flask
from Framework_AC4.Clientes_model import Clientes_model


app = Flask(__name__)

@app.route('/consultar_Clientes/', methods=["GET"])
def consultar_Clientes():
    return Clientes_model.clientes()




if __name__ == '__main__':
    app.run(debug=True,port= 5000)