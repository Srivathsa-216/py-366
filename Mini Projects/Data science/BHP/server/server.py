from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get-location-names')
def hello():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-origin','*')

    return "Hi"

if __name__ == "__main__":
    print("Starting Python Flask server for Home Price Prediction....")
    app.run()