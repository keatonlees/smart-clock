from flask import Flask, render_template, jsonify
import requests
import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_update_time', methods=['POST'])
def update_time():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M")
    })

@app.route('/_update_date', methods=['POST'])
def update_date():
    return jsonify({
        'date': datetime.datetime.now().strftime("%A, %B %d")
    })

@app.route('/_get_alarm', methods=['POST'])
def get_day():
    return jsonify({
        'time': datetime.datetime.now().strftime("%H:%M:%S"),
        'day': datetime.datetime.now().strftime("%A")
    })

@app.route('/_update_weather', methods=['POST'])
def update_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=bd44a2b2a80b02693d0e10ee79e6ecdb'
    location = 'South Surrey'
    
    r = requests.get(url.format(location)).json()
    
    return jsonify({
        'location': location,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
