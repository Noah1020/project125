from flask import Flask, request, jsonify
from project125 import get_prediction

app = Flask(__name__)

@app.route("/predict_letter", methods = ["POST"])
def predict_digit():
    image = request.files.get("letter")
    prediction = get_prediction(image)
    return jsonify({"predicted_letter":prediction}), 200

if(__name__ == "__main__"):
    app.run(debug = False)

