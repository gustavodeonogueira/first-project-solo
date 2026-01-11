from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "SRE service is running"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/slow")
def slow():
    time.sleep(5)
    return "slow response"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
