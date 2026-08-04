app.py
from flask import Flask, render_template, request
from weather import get_current_weather, get_forecast_5days

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        weather = get_current_weather(city)
    return render_template("index.html", weather=weather)

@app.route("/5_days/<city>")
def forecast_5days(city):
    forecast = get_forecast_5days(city)
    return render_template("5_days.html", forecast=forecast, city=city)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
