@app.route("/", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        data = pd.read_csv('data.csv')
        print('eat my booty please')
        idea = random.choice(data['Ideas'])
        return render_template("index.html", idea = idea)
    else:
        return render_template("index.html", idea="eat my booty")



@app.route("/", methods=["POST", "GET"])
def generate():
    data = pd.read_csv('data.csv')
    print('eat my booty please')
    idea = random.choice(data['Ideas'])
    return render_template("index.html", idea = idea)   