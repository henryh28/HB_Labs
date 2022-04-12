"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route("/")
def start_here():
    """Display homepage."""

    return "<a href='/greet'> Play a game? </a>"

@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    return render_template("compliment.html")


@app.route("/game")
def show_madlib_form():
    """ Plays a game of madlib """

    return render_template("game.html" if request.args.get('play_game') == "yes" else "goodbye.html")

@app.route("/madlib")
def show_mad_lib():
    """ Displays the result of the madlib """

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    return render_template("madlib.html", person = person, color = color, noun = noun, adjective = adjective)





if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
