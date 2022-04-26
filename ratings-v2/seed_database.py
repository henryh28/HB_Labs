""" Seeds database with demo data """

import os, json, model, server, crud
from random import choice, randint
from datetime import datetime as dt

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    release_date = dt.strptime(movie["release_date"], "%Y-%m-%d")
    movies_in_db.append(crud.create_movie(movie["title"], movie["overview"], release_date, movie["poster_path"]))

model.db.session.add_all(movies_in_db)
model.db.session.commit()



for n in range(10):
    email = f"user{n}@test.com"
    password = "test"

    temp_user = crud.create_user(email, password)
    model.db.session.add(temp_user)

    for i in range(10):
        temp_rating = crud.create_rating(randint(1, 5), temp_user, choice(movies_in_db))
        model.db.session.add(temp_rating)

model.db.session.commit()
