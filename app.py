from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Dummy AI function (to be replaced with your trained model)
def predict_next_number(sequence):
    return sequence[-1] + (sequence[1] - sequence[0])  # Basic pattern detection

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        sequence = list(map(int, request.form["sequence"].split(",")))
        prediction = predict_next_number(sequence)
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
