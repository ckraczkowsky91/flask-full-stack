from application import app
from flask import render_template

# Creating some default routes
@app.route('/')
@app.route('/index')
@app.route('/barf')
def index():
    return render_template('index.html')
