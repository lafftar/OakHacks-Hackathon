from flask import render_template, Flask, request, jsonify
from flask_cors import CORS
from backend.api_methods import get_fin_data, get_tweets
from time import time


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/api/v1/get_financial_data', methods=['GET'])
def return_fin_data():
    return jsonify(get_fin_data(request.args["username"]))


@app.route('/api/v1/get_tweets', methods=['GET'])
def return_tweets():
    return jsonify(get_tweets(request.args["username"]))


@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')



app.run()
