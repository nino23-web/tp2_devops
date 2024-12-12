from flask import Flask
import yaml
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # Simulation d'un traitement utilisant des dépendances vulnérables
    data = yaml.load("key: value", Loader=yaml.FullLoader)  # PyYAML vulnérable
    response = requests.get("http://example.com")  # Utilise requests obsolète
    return f"Response from example.com: {response.status_code}, Parsed YAML: {data}"

if __name__ == "__main__":
    app.run(debug=True)
