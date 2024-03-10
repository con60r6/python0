from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def start():
    response = requests.get("https://api.github.com")
    return '1 2 3 4 5 6 7 8 9 0'# + str(response.status_code)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
