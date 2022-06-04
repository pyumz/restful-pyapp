from app import app, database
from flask_cors import CORS
from flasgger import Swagger

CORS(app, resources={r"/*": {"origins":"*"}})

app.config['SWAGGER'] = {
    'title': 'Games API',
    'version': '1.0'
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": '',
            "route": '/swagger.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

swagger = Swagger(app, config=swagger_config)
