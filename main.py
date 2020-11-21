from flask import Flask, render_template
import datetime

app = Flask(__name__)
@app.route("/")

def index():
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M")
    
    template_data = {
        'title' : 'TEST!',
        'time' : time_str
        }
    
    return render_template('index.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)