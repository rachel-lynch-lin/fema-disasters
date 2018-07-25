"""Models and database functions for California Disaster project"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

###############################################################################
# Model definitions


class Event(db.Model):
    """The disaster events that occured in California"""

    __tablename__ = "events"

    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    fema_id = db.Column(db.ForeignKey('disasters.fema_id'))

    name = db.Column(db.String, nullable=True)

    start_date = db.Column(db.DateTime, nullable=False)

    end_date = db.Column(db.DateTime, nullable=True)

    type_id = db.Column(db.ForeignKey('types.type_id'))

    county_id = db.Column(db.ForeignKey('locations.county_id'))

    def __repr__(self):
        """Display info about the disaster event"""

        return f"""Event ID: {self.event_id}
                   Location: {self.locations}
                   Name: {self.name}
                   Disaster Event: {self.type_name}
                   Occured On: {self.start_date}"""


class Type(db.Model):
    """Types of disasters that have occured in California"""

    __tablename__ = "types"

    type_id = db.Column(db.String(25), primary_key=True)  # Take from types

    type_name = db.Column(db.String(25))  # Take from type_name

    def __repr__(self):
        """Display type of disaster"""

        return f"""Type ID: {self.type_id}
                   Type Name: {self.type_name}"""


class Location(db.Model):
    """The location that the disaster took place in California"""

    __tablename__ = "locations"

    county_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    counties = db.Column(db.String)

    zipcodes = db.Column(db.Integer)

    def __repr__(self):
        """Display type of disaster"""

        return f"""County ID: {self.county_id}
                   County Name:{self.counties}
                   Zipcodes: {self.zipcodes}"""
    # Create a dictionary for locations. key(county): value(zipcodes)
    # Will allow for greater user interactivity later.


class Fema(db.Model):
    """Links ID provided by FEMA to event and if money was awarded"""

    __tablename__ = "disasters"

    fema_id = db.Column(db.String, primary_key=True)

    event_id = db.Column(db.ForeignKey('events.event_id'))

    pa_grant_total = db.Column(db.Float(scale=2))

    def __repr__(self):
        """Display type of disaster"""

        return f"""FEMA ID:{self.fema_id}
                   Public Assistance Total Grant: ${self.pa_grant_total}."""


class PropertyDamage(db.Model):
    """For each disaster event this checks if property damaged occured"""

    __tablename__ = "damages"

    damage_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    event_id = db.Column(db.ForeignKey('events.event_id'))

    fema_id = db.Column(db.ForeignKey('disasters.fema_id'))

    damaged_property = db.Column(db.Boolean)

    def __repr__(self):
        """Display type of disaster"""

        return f"""Damage ID: {self.damage_id}
                   Event ID: {self.event_id}
                   FEMA ID: {self.fema_id}
                   Damaged Property: {self.damaged_property}"""


###############################################################################

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///disasters'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to DB.")
    db.create_all()
