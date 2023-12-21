from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from Data.seeder import start_up  

from Routes.parameters import parameter_blueprint
from Routes.players import players_blueprint

app = Flask(__name__)
start_up()

# http://localhost:5000/apidocs/
Swagger(app)
CORS(app)

app.register_blueprint(parameter_blueprint)
app.register_blueprint(players_blueprint)

if __name__ == "__main__":
    app.debug = True
    app.run() 