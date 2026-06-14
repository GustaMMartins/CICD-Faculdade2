from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "API rodando muito bem!"
<<<<<<< HEAD

@app.route("/status")
def status():
    return {"status": "ok"}

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return {"resultado": a + b}
=======
>>>>>>> 1c4aa8baed265a9b49b432ca005046e75efa6d74

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)