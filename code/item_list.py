from flask_restful import Resource
from flask_jwt import jwt_required

import sqlite3

class ItemList(Resource):
    TABLE_NAME = 'items'
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.sqlite3')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'items': items}