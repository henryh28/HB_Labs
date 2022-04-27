"""Server for movie ratings app."""

from urllib import response
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route("/")
def homepage():
    """ View Homepage """

    if 'user' not in session:
        session['user'] = None
    


    return render_template("homepage.html")


# Movie related routes
@app.route("/movies")
def get_all_movies():
    """ Displays all movies in database """

    all_movies = crud.get_all_movies()

    return render_template("all_movies.html", all_movies = all_movies)


@app.route("/movies/<movie_id>")
def view_movie_detail(movie_id):
    """ Display info for specified movie """

    movie = crud.get_single_movie(movie_id)

    return render_template("movie_details.html", movie = movie)



# User related routes
@app.route("/users")
def get_all_users():
    """ Displays all users in database """

    all_users = crud.get_all_users()

    return render_template("all_users.html", all_users = all_users)


@app.route("/users", methods = ["POST"])
def register_user():
    """ Create a  user """

    email = request.form.get("email")
    password = request.form.get("password")

    if crud.get_user_by_email(email):
        flash(f"Cannot create account using {email} as that email address has already been used by existing account")
    else:
        new_user = crud.create_user(email, password)
        db.session.add(new_user)
        db.session.commit()
        flash(f"Successfuly created account!")

    return redirect("/")


@app.route("/users/<user_id>")
def view_user_detail(user_id):
    """ Display info for specified user """

    user = crud.get_single_user(user_id)

    return render_template("user_details.html", user = user)


@app.route("/login", methods = ["POST"])
def login_user():
    """ Authenticates user for login """

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        if user.password == password:
            flash(f"Logged in!")
            session['user'] = user.user_id
        else:
            flash(f"Invalid password")
    else:
        flash(f"No matching user found")

    return redirect("/")


@app.route("/rate_movie/<movie_id>")
def rate_movie(movie_id):
    """ Rates a movie """

    score = request.args.get("vote")
    user = crud.get_single_user(session['user'])
    movie = crud.get_single_movie(movie_id)

    new_rating = crud.create_rating(score, user, movie)
    db.session.add(new_rating)
    db.session.commit()

    return redirect(f"/movies/{movie_id}")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
