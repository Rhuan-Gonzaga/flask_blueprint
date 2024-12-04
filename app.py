from flask import Flask
from produtos.produtos import produtos_blueprint
from pedidos.pedidos import pedidos_blueprint

app = Flask(__name__)
app.register_blueprint(produtos_blueprint)
app.register_blueprint(pedidos_blueprint)
