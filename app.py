import pandas as pd
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        data = pd.read_csv('data.csv')
        print('eat my booty please')
        idea = random.choice(data['Ideas'])
        return render_template("index.html", idea = idea)
    else:
        return render_template("index.html", idea="Eat my booty") 

if __name__ == "__main__":
    app.run(debug=True)