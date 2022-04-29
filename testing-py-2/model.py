from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///testdb"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""

    db.session.add(Game(name = "Wingspan", description = "Attract a beautiful and diverse collection of birds to your wildlife reserve."))
    db.session.add(Game(name = "Viticulture", description = "Create the most prosperous winery in Italy from the Tuscan vineyard you've inherited."))
    db.session.add(Game(name = "Scoville", description = "A plunge into a pepper planters plan, strategize your field to win the chili contest!"))
#    db.session.add(Game(name = "Wingspan", description = "Attract a beautiful and diverse collection of birds to your wildlife reserve."))
#    db.session.add(Game(name = "Marvel Champions - The Card Game", description = "Battle Marvel villains with unique teams of iconic heroes in this LCG."))
    db.session.commit()
    

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
