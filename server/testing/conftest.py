import pytest
from server.app import app
from server.models import db


@pytest.fixture(scope='function', autouse=True)
def setup_db():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()
