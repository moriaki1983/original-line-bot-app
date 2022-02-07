
from flask import Flask
from werkzeug.wrappers import Response

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world!"

def application(environ, start_response):
    response = Response('Hello World!', mimetype='text/plain')
    return response(environ, start_response)

if __name__ == "__main__":
    app.run()
