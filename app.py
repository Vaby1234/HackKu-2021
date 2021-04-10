import pandas as pd
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        data = pd.read_csv('data.csv')
        print('A spectre is haunting Europe – the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre: Pope and Tsar, Metternich and Guizot, French Radicals and German police-spies. Where is the party in opposition that has not been decried as communistic by its opponents in power? Where is the opposition that has not hurled back the branding reproach of communism, against the more advanced opposition parties, as well as against its reactionary adversaries? Two things result from this fact: I. Communism is already acknowledged by all European powers to be itself a power. II. It is high time that Communists should openly, in the face of the whole world, publish their views, their aims, their tendencies, and meet this nursery tale of the Spectre of Communism with a manifesto of the party itself. To this end, Communists of various nationalities have assembled in London and sketched the following manifesto, to be published in the English, French, German, Italian, Flemish and Danish languages.')
        idea = random.choice(data['Ideas'])
        return render_template("index.html", idea = idea)
    else:
        return render_template("index.html", idea="Give Me Sauce") 

if __name__ == "__main__":
    app.run(debug=True)