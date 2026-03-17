from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from server.models import db, Hero, Power

app = Flask(__name__)
CORS(app)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///heroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database with this app
db.init_app(app)
Migrate(app, db)

# ROUTES


@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(rules=('-hero_powers',)) for hero in heroes]), 200


@app.route("/heroes/<int:id>", methods=["GET"])
def get_hero_by_id(id):
    hero = db.session.get(Hero, id)
    if hero:
        return jsonify(hero.to_dict()), 200
    return jsonify({"error": "Hero not found"}), 404


@app.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200


if __name__ == "__main__":
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
