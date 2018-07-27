"""Models and database functions for California Disaster project"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

###############################################################################
# Model definitions


class Event(db.Model):
    """The disaster events that occured in California"""

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    fema_id = db.Column(db.String, nullable=False)

    name = db.Column(db.String, nullable=True)

    start_date = db.Column(db.DateTime, nullable=False)

    end_date = db.Column(db.String, nullable=True)  # Change to Datetime later

    damaged_property = db.Column(db.String, default="Unknown")

    pa_grant_total = db.Column(db.Float)

    type_id = db.Column(db.ForeignKey('types.id'))

    county_id = db.Column(db.ForeignKey('locations.id'))

    def __repr__(self):
        """Display info about the disaster event"""

        return f"""<Event ID: {self.id}
                   FEMA ID: {self.fema_id}
                   Location: {self.county_id}
                   Name: {self.name}
                   Disaster Event: {self.type_id}
                   Occured On: {self.start_date}
                   Ended On: {self.end_date}
                   Damaged Property: {self.damaged_property}
                   Public Assistance Total Grant: ${self.pa_grant_total}>"""


class Type(db.Model):
    """Types of disasters that have occured in California"""

    __tablename__ = "types"

    id = db.Column(db.String(25), primary_key=True)  # Take from types

    type_name = db.Column(db.String(25))  # Take from type_name

    def __repr__(self):
        """Display type of disaster"""

        return f"""<Type ID: {self.id}
                   Type Name: {self.type_name}>"""


class Location(db.Model):
    """The location that the disaster took place in California"""

    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    state = db.Column(db.String)

    county = db.Column(db.String)

    def __repr__(self):
        """Display type of disaster"""

        return f"""<County ID: {self.id}
                   State: {self.state}
                   County Name:{self.county}>"""


class User(db.Model):
    """Keep user info to save user info and searches"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String, nullable=False)

    email = db.Column(db.String, unique=True, nullable=False)

    password = db.Column(db.String, nullable=False)

    occupation = db.Column(db.String)

    def __repr__(self):
        """Display information about the user"""

        return f"""<User ID: {self.id}
                   Username: {self.username}
                   Email: {self.email}
                   Password: {self.password}
                   Occupation: {self.occupation}>"""

###############################################################################

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///disasters'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
    db.create_all()
