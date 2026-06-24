from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Grafana Monitoring Demo"

@app.route("/api")
def api():
    time.sleep(random.uniform(0.1, 1.0))
    return {"status": "success"}

if __name__ == "__main__":
    app.run(port=5000)