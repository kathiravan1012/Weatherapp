from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'f51b94063fe732a94d0a0baaf074f33d'  

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        return render_template('index.html', weather=weather)
    return render_template('index.html', weather=None)

if __name__ == '__main__':
    app.run(debug=True)
