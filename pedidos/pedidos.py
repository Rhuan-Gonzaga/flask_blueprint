from flask import Blueprint, render_template

pedidos_blueprint = Blueprint('pedidos',__name__, template_folder='templates')

@pedidos_blueprint.route('/pedidos')
def lista_pedidos():
  return render_template('lista_pedidos.html')