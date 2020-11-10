from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_cors import CORS
from predict_types import predict_type,recreate_model, predict_tweet, predict_follow
from twitterscraper import tweet_return

app = Flask(__name__, static_folder="static")
CORS(app)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/predict', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        data = request.get_json()  # parse as JSON
        user_text = data["data"]
        user_type = predict_type(user_text)
        return jsonify({"type":str(user_type)}),200

@app.route('/tweet_pred', methods=['GET', 'POST'])
def tweet():
    # GET request
    if request.method == 'GET':
        return render_template('dashboard.html')
    # POST request
    if request.method == 'POST':
        data = request.get_json()  # parse as JSON
        user_handle = data["handle"]
        tweet_return(user_handle)
        user_type = predict_tweet(user_handle)
        # render_template('result.html')
        return jsonify(user_type),200

@app.route('/follow_pred', methods=['GET', 'POST'])
#endpoint to fetch user followers
def follow_tweet():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        data = request.get_json()  # parse as JSON
        user_handle = data["handle"]
        # tweet_return(user_handle)
        user_type = predict_follow(user_handle)
        return jsonify({"type":str(user_type)}),200

if __name__ == '__main__' :
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True, port=5000)