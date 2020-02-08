import os
from flask import Flask, render_template
import config

app = Flask(__name__)

#app.config.from_object(Config())
app.config['DATABASE'] = os.path.join(app.instance_path, 'flask-app.sqlite')

try:
	os.makedirs(app.instance_path)
except OSError:
	pass

@app.route('/')
def hello():
    #return "Hello World!"
    return render_template("index.html",title="Home")

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

import db
db.init_app(app)

if __name__ == '__main__':
    app.run()