## Code boilerplate

```
from flask_jwt import JWT
jwt = JWT(app, authenticate, identity)

app.secret_key = 'SeRet' # Jwt use it

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)

```

## Use the token
    add Authorization into http headers
     Authorization : JWT <token>

