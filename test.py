from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

menu = {
    "Pizza": 25.0,
    "Pâtes": 20.0,
    "Salade": 15.0,
    "Burger": 22.0,
    "Tiramisu": 10.0
}


@app.route("/")
def home():
    return render_template("index.html", menu=menu)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
