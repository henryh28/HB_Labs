"""Greeting Flask app."""

from random import choice

from flask import Flask, request, render_template

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

Insults = ['mean', 'condescending', 'annoying', 'unkind']

@app.route('/')
def start_here():
    """Home page."""


    return "<!doctype html><html>Hi! This is the home page.      <a href='/hello'>Say hi to me</a> <br> <a href='diss'>Diss me</a>   </html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>

          <label for="compliment">What is your preferred compliment?</label>
          <select name="compliment" id="compliment">
            <option value="kind">Kind</option>
            <option value="ethical">Ethical</option>
            <option value="considerate">Considerate</option>
          </select><br>

          What is your second compliment?<br>
          <input type="radio" id="happy" name="compliment2" value="Happy!">
          <label for="happy">Happy</label><br>
          <input type="radio" id="thoughtful" name="compliment2" value="Thoughtful :)">
          <label for="thoughtful">Thoughtful</label><br>
          <input type="radio" id="supportive" name="compliment2" value="so supportive!">
          <label for="supportive">Supportive</label><br>

          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
  
    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")
    compliment2 = request.args.get("compliment2")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment} and also {compliment2}!
      </body>
    </html>
    """



@app.route('/diss')
def diss():
  return render_template('/diss.html')


@app.route('/dissme')
def dissme():
    """Insult user."""

    player = request.args.get("person")

    insult = choice(Insults)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Yo {player}! I think you're {insult}!
      </body>
    </html>
    """  


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
