from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

# RESTful resources
from user import UserRegister
from item import Item
from item_list import ItemList


def create_app(**config_overrides):
    app = Flask(__name__)
    # read config file
    app.config.from_pyfile('config.py')
    app.config.update(config_overrides)

    api = Api(app)

    jwt = JWT(app, authenticate, identity)

    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(UserRegister, '/register')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # important to mention debug=True
