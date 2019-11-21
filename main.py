from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/barf')
def index():
    return '<h1>Hiyee again!</h1>'
