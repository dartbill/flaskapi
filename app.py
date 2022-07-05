from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import cats
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# db = SQLAlchemy(app)

# class Item(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(80), unique=True, nullable=False)
#   content = db.Column(db.String(120), unique=True, nullable=False)

#   def __init__(self, title, content):
#     self.title = title
#     self.content = content

# db.create_all()

@app.route('/items/<id>', methods=['GET'])
def get_item(id):
  item = Item.query.get(id)
  del item.__dict__['_sa_instance_state']
  return jsonify(item.__dict__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/cats', methods=['GET', 'POST'])
def cats_handler():
    fns = {
        'GET': cats.index,
        'POST': cats.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/cats/<int:cat_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def cat_handler(cat_id):
    fns = {
        'GET': cats.show,
        'PATCH': cats.update,
        'PUT': cats.update,
        'DELETE': cats.destroy
    }
    resp, code = fns[request.method](request, cat_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)