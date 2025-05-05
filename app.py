from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# SQLite DB configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(BASE_DIR, 'db')
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

db_path = os.path.join(db_dir, 'plans.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Recharge Plan model
class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    validity = db.Column(db.String(50), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/plans', methods=['POST'])
def add_plan():
    data = request.json
    name = data.get('name')
    price = data.get('price')
    validity = data.get('validity')
    new_plan = Plan(name=name, price=price, validity=validity)
    db.session.add(new_plan)
    db.session.commit()
    return jsonify({'message': 'Plan added successfully'}), 201

@app.route('/plans', methods=['GET'])
def list_plans():
    all_plans = Plan.query.all()
    result = [{'id': p.id, 'name': p.name, 'price': p.price, 'validity': p.validity} for p in all_plans]
    return jsonify(result), 200

@app.route('/plans/<int:plan_id>', methods=['DELETE'])
def delete_plan(plan_id):
    plan = Plan.query.get(plan_id)
    if not plan:
        return jsonify({'message': 'Plan not found'}), 404
    db.session.delete(plan)
    db.session.commit()
    return jsonify({'message': f'Plan {plan_id} deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

