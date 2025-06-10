from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Dummy function for pattern recognition & prediction
# def predict_sequence(sequence):
#     sequence = np.array(sequence).reshape(-1, 1)
#     indices = np.arange(len(sequence)).reshape(-1, 1)

#     model = LinearRegression()
#     model.fit(indices, sequence)

#     future_indices = np.arange(len(sequence), len(sequence) + 5).reshape(-1, 1)
#     predictions = model.predict(future_indices)
    

#     return predictions.flatten().tolist()
# def predict_sequence(sequence):
#     sequence = np.array(sequence).reshape(-1, 1)
#     indices = np.arange(len(sequence)).reshape(-1, 1)

#     model = LinearRegression()
#     model.fit(indices, sequence)

#     future_indices = np.arange(len(sequence), len(sequence) + 5).reshape(-1, 1)
#     predictions = model.predict(future_indices)

#     # Convert to integer format by rounding
#     return [round(num) for num in predictions]

# def predict_sequence(sequence):
#     sequence = np.array(sequence).reshape(-1, 1)
#     indices = np.arange(len(sequence)).reshape(-1, 1)

#     model = LinearRegression()
#     model.fit(indices, sequence)

#     future_indices = np.arange(len(sequence), len(sequence) + 5).reshape(-1, 1)
#     predictions = model.predict(future_indices)

#     # Convert NumPy array to a list, then round each number
#     return [round(float(num)) for num in predictions.tolist()]

def predict_sequence(sequence):
    sequence = np.array(sequence).reshape(-1, 1)
    indices = np.arange(len(sequence)).reshape(-1, 1)

    model = LinearRegression()
    model.fit(indices, sequence)

    future_indices = np.arange(len(sequence), len(sequence) + 5).reshape(-1, 1)
    predictions = model.predict(future_indices)

    # Ensure proper list conversion before rounding
    return [round(float(num)) for num in predictions.flatten()]



# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         sequence = list(map(float, request.form.get("sequence").split(",")))
#         predictions = predict_sequence(sequence)
#         return render_template("index.html", predictions=predictions)

#     #return render_template("index.html")
#     return render_template("index.html", predictions=[round(num, 2) for num in predictions])

@app.route("/", methods=["GET", "POST"])
def index():
    predictions = []  # Initialize predictions to avoid UnboundLocalError

    if request.method == "POST":
        sequence_input = request.form.get("sequence")

        if sequence_input:  # Ensure input isn't empty
            sequence = list(map(float, sequence_input.split(",")))
            predictions = predict_sequence(sequence)

    return render_template("index.html", predictions=predictions)


if __name__ == "__main__":
    app.run(debug=True)
