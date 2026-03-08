from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table for many-to-many Hero <-> Power
hero_powers = db.Table(
    "hero_powers",
    db.Column("hero_id", db.Integer, db.ForeignKey("heroes.id"), primary_key=True),
    db.Column("power_id", db.Integer, db.ForeignKey("powers.id"), primary_key=True)
)

class Hero(db.Model):
    __tablename__ = "heroes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    powers = db.relationship(
        "Power",
        secondary=hero_powers,
        back_populates="heroes"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "powers": [power.to_dict() for power in self.powers]
        }

class Power(db.Model):
    __tablename__ = "powers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    heroes = db.relationship(
        "Hero",
        secondary=hero_powers,
        back_populates="powers"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }