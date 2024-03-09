from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def start():
    response = requests.get("https://api.github.com")
    return 'Hello world!'# + str(response.status_code)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
