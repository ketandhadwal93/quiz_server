from flask import Flask, request

right_answer_counter = 0
wrong_answer_counter = 0

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


# request will be sent as http://127.0.0.1:5000/question2?answer=yes
@app.route("/question2")  # /question2 is called an api end point
def cpu():
    answer = request.args.get('answer')
    if answer == "central processing unit":
        right_answer_counter = right_answer_counter + 1
        return (f"<p>Correct!</p>", 200)
    else:
        wrong_answer_counter = wrong_answer_counter + 1
        return (f"<p>Incorrect!</p>", 200)


# request will be sent as http://127.0.0.1:5000/question3?answer=yes
@app.route("/question3")  # /question3 is called an api end point
def gpu():
    answer = request.args.get('answer')
    if answer == "graphical processing unit":
        right_answer_counter = right_answer_counter + 1
        return (f"<p>Correct!</p>", 200)
    else:
        wrong_answer_counter = wrong_answer_counter + 1
        return (f"<p>Incorrect!</p>", 200)

# request will be sent as http://127.0.0.1:5000/question4?answer=yes
@app.route("/question4")  # /question4 is called an api end point
def capitalcity():
    answer = request.args.get('answer')
    if answer == "delhi":
        right_answer_counter = right_answer_counter + 1
        return (f"<p>Correct!</p>", 200)
    else:
        wrong_answer_counter = wrong_answer_counter + 1
        return (f"<p>Incorrect!</p>", 200)
