from flask import render_template, Flask, request, jsonify
from flask_cors import CORS
from time import time


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/api/v1/search', methods=['GET'])
def search():
    return 'test'

@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')



app.run()
