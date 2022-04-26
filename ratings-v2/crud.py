""" Define CRUD operations for project database """

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime as dt


def create_user(email, password):
    """Create and return a new user."""
    return User(email=email, password=password)

def create_movie(title, overview, release_date, poster_path):
    """ Create and return a new movie """
    return Movie(title = title, overview = overview, release_date = release_date, poster_path = poster_path)

def create_rating(score, user, movie):
    """ Create and return a new rating """
    return Rating(score = score, user = user, movie = movie)



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
