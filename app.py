from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>\"Welcome to my Quiz!<br><br>Do you want to play?\"</p>"

# request will be sent as http://127.0.0.1:5000/doyouwanttoplay?answer=yes
@app.route("/question1")  # /doyouwanttoplay is called an api end point
def do_you_want_to_play():
    playing = request.args.get('answer')
    print(f"playing?: {playing}")
    if playing != "yes":
        return("<p>Bye!</p>", 200)
    return (f"<p>\"Okay, Let's play!! {request.args.get('name')}\"</p>", 200)


