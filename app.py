from flask import Flask, render_template, request
import requests # pip install requests

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/weatherapp", methods=["POST"])
def get_weather_data():
    apikey = 'b2f7276693524dc1283929277faa0eae'
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q' : request.form.get("city"),
        'appid' : request.form.get("appid"),
        'units' : request.form.get("units")
    }
    response = requests.get(url, params=params)
    data = response.json()
    city=data['name']
    return f"data: {data}, city: {city}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

