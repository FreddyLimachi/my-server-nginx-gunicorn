from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style='color:#139E00'>Server running</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')


    