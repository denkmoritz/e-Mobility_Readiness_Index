import os
import yaml

# Define the path to the pygeoapi configuration and OpenAPI documents
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "pygeoapi-config", "pygeoapi-config.yml")
OPENAPI_PATH = os.path.join(os.path.dirname(__file__), "pygeoapi-config", "openapi.yml")  # Adjust if needed

# Set required environment variables BEFORE importing PyGeoAPI
os.environ["PYGEOAPI_CONFIG"] = CONFIG_PATH  # Set PyGeoAPI config path
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)
    print("Loaded PyGeoAPI Config:", config)  # Print the config on startup
os.environ["PYGEOAPI_OPENAPI"] = OPENAPI_PATH  # Set OpenAPI document path

# Now import Flask and PyGeoAPI
from flask import Flask
from pygeoapi.flask_app import BLUEPRINT as pygeoapi_blueprint

# Initialize the Flask app
app = Flask(__name__)

# Register PyGeoAPI as a blueprint under '/oapi'
app.register_blueprint(pygeoapi_blueprint, url_prefix='/oapi')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3456)