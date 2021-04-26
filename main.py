import flask
from flask_cors import CORS
from flask import Flask
from main_hw import app_hw

app = Flask(__name__)
app.register_blueprint(app_hw)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

@app.route('/Cov')
def nCovnxtworld():
    return flask.send_from_directory('static', 'Cov-world.html')


@app.route('/static/<fname>')
def sendfile(fname):
    return flask.send_from_directory('static', fname)

app.run(host='0.0.0.0', port=12345, debug=True)
