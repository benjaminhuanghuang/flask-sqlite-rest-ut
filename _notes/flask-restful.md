## Refernce
    https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
    
## Code boilerplate
    ```
    from flask import Flask
    from flask.ext.restful import Api, Resource
    
    app = Flask(__name__)
    api = Api(app)
    
    class UserAPI(Resource):
        def get(self, id):
            pass
    
        def put(self, id):
            pass
    
        def delete(self, id):
            pass
    
    api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')
    ```
    - Resource class can define the routing for one or more HTTP methods for a given URL.
    - add_resource function registers the routes with the framework using the given endpoint
    
## Request parsing
    Flask
    ```
    from flask import request
    
    data = request.get_json()
    newItem = {'name': name,  'price':data['price']}
    ```
    
    Flask-RESTful
    ```
    from flask_restful import reqparse 
    
    parser = reqparser.RequestParser();
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    data = parse.parse_args()
    newItem = {'name': name, 'price': data['price']}
    
    ```
    
## Response
    Flask-RESTful automatically handles the conversion to JSON, so instead of this:
    ```
        return jsonify( { 'task': make_public_task(task) } )
    ```   
    We can do this:
    ```
        return { 'task': make_public_task(task) }, 201
    ```