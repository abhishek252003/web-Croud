from flask import Flask, request, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)
traffic_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    url = request.form['website_url']
    return render_template('dashboard.html', website=url)

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    data['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    traffic_data.append(data)
    return '', 204

@app.route('/live-data')
def live_data():
    return jsonify(traffic_data[-10:])  # Send last 10 visits

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
