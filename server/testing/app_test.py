import pytest
from faker import Faker
from server.app import app
from server.models import db, Hero

class TestApp:

    def test_gets_heroes(self):
        with app.app_context():
            fake = Faker()
            hero1 = Hero(name=fake.name(), super_name=fake.name())
            hero2 = Hero(name=fake.name(), super_name=fake.name())
            db.session.add_all([hero1, hero2])
            db.session.commit()

            response = app.test_client().get("/heroes")
            assert response.status_code == 200
            data = response.json
            assert len(data) >= 2

    def test_gets_hero_by_id(self):
        with app.app_context():
            fake = Faker()
            hero = Hero(name=fake.name(), super_name=fake.name())
            db.session.add(hero)
            db.session.commit()

            response = app.test_client().get(f"/heroes/{hero.id}")
            assert response.status_code == 200
            data = response.json
            assert data["id"] == hero.id
            assert data["name"] == hero.name
            assert data["super_name"] == hero.super_name
            assert "powers" in data