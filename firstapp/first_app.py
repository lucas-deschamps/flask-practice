from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

# my first Flask project
# it's a simple webpage that prints out random quotes
# the quote page prints out the name that went into the URL (e.g. /hello/Marcos will display "Hello, Marcos")
# the quote page also prints out a random quote from its list

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1><a href=\"http://localhost:5000/hello/world/\">Welcome</a>, world!</h1>"

@app.route("/hello/<string:name>/")
def hello(name):

    quotes = [
    '"Computer science is no more about computers than astronomy is about telescopes." — Edsger Dijkstra',
    '"To understand recursion you must first understand recursion." — Unknown',
    '"Mathematics is the key and door to the sciences." — Galileo Galilei',
    '"Not everyone will understand your journey. That\'s fine. It\'s not their journey to make sense of. It\'s yours." — Unknown'
             ]

    random = randint(0, len(quotes)-1)
    quote = quotes[random]

    return render_template('test.html', **locals())

# members/(member(name))/
@app.route("/members/<string:name>/")
def getMember(name):
    return f"Member: {name}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
