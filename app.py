from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        # ... [Your previous code for processing form data] ...

        # Perform the prediction using the model
        prediction = model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            # ... and other input features for your model
        ]])

        # Convert the prediction from Rupees to Euros (assuming the output is in Rupees)
        output_in_rupees = prediction[0]
        output_in_euros = output_in_rupees * 0.011  # Conversion rate from Rupees to Euros
        output_in_euros = round(output_in_euros, 2)

        # Pass the converted price to the rendered template in Euros
        return render_template('home.html', prediction_text=f"Your Flight price is € {output_in_euros}")

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
