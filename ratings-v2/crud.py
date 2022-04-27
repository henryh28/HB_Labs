""" Define CRUD operations for project database """

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime as dt


# ========= User related functions ==========
def create_user(email, password):
    """Create and return a new user."""

    return User(email=email, password=password)


def get_all_users():
    """ Return a list containing all users in database """
    return User.query.all()

def get_single_user(user_id):
    """ Return info pertaining to specified user """
    return User.query.get(user_id)

def get_user_by_email(email):
    """ Search for existing user by provided email """
    return User.query.filter(User.email == email).first()


# ========= Movie related functions ==========
def create_movie(title, overview, release_date, poster_path):
    """ Create and return a new movie """
    return Movie(title = title, overview = overview, release_date = release_date, poster_path = poster_path)


def get_all_movies():
    """ Return a list containing all movies in database """
    return Movie.query.all()

def get_single_movie(movie_id):
    """ Return info pertaining to specified movie """
    return Movie.query.get(movie_id)

# ========= Rating related functions ==========
def create_rating(score, user, movie):
    """ Create and return a new rating """
    return Rating(score = score, user = user, movie = movie)



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
