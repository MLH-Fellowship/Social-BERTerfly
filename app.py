from flask import Flask, render_template, request, redirect, url_for

#from get_tweets import get_related_tweets

#pipeline = load("text_classification.joblib")

app = Flask(__name__)


@app.route('/predict', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

if __name__ == '__main__' :
    app.run(debug=True)

