"""File to seed the tables created in model.py from the files in seed_data/"""

from sqlalchemy import func
from model import Event, Type, Location
from model import connect_to_db, db

from datetime import datetime
# from server import app


def load_events():
    """Load events from event.txt into the database"""

    print("Events")

    # Delete rows in the table to prevent duplicates if run twice
    Event.query.delete()

    # Read event.txt, organize data, and insert data
    for row in open("seed_data/event.txt"):
        row = row.rstrip()

        row = row.split("|")
        # Add list comprehension here in a later version of this file
        for index, value in enumerate(row):
            if value == "":
                row[index] = None

        # row = [None for value in row if value == ""]

        fema_id, name, start_date, end_date, damaged_property, pa_grant_total = row

        events = Event(fema_id=fema_id,
                       name=name,
                       start_date=start_date,
                       end_date=end_date,
                       damaged_property=damaged_property,
                       pa_grant_total=pa_grant_total)

        # Add event to the session to be stored
        db.session.add(events)

    # Commit changes
    db.session.commit()


def load_types():
    """"""

    print("Types")

    Type.query.delete()

    for row in open("seed_data/type.txt"):
        row = row.rstrip()
        id, type_name = row.split("|")

        types = Type(id=id,
                     type_name=type_name)

        db.session.add(types)

    db.session.commit()


def load_locations():
    """"""

    print("Locations")

    Location.query.delete()

    for row in open("seed_data/location.txt"):
        row = row.rstrip()
        print(row)
        state, county = row.split("|")

        locations = Location(state=state,
                             county=county)

        db.session.add(locations)

    db.session.commit()


if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to DB.")
    db.create_all()
    # Import different types of data
    load_events()
    load_types()
    load_locations()
