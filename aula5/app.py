from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "SLK, merece um 10, Meu código roda tão liso que a RAM pede férias!"

@app.route("/status")
def status():
    return {"status": "ok"}

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return {"resultado": a + b}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)