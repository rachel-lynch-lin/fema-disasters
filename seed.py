"""File to seed the tables created in model.py from the files in seed_data/"""

from sqlalchemy import func
from model import Event, Type, Location, Fema, PropertyDamage
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
        fema_id, name, start_date, end_date = row.split("|")

        event = Event(name=name,
                      start_date=start_date)  # end_date=end_date)

        # Add event to the session to be stored
        db.session.add(event)

    # Commit changes
    db.session.commit()


def load_types():
    """"""

    print("Types")

    Type.query.delete()

    for row in open("seed_data/type.txt"):
        row = row.rstrip()
        type_id, type_name = row.split("|")

        types = Type(type_id=type_id,
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
        states, counties, cities, zipcodes = row.split("|")

        location = Location(states=states,
                            counties=counties,
                            cities=cities,
                            zipcodes=zipcodes)

        db.session.add(location)

    db.session.commit()


def load_fema():
    """"""

    print("FEMA")

    Fema.query.delete()

    for row in open("seed_data/fema.txt"):
        row = row.rstrip()
        fema_id, pa_grant_total = row.split("|")

        fema = Fema(fema_id=fema_id,
                    pa_grant_total=pa_grant_total)

        db.session.add(fema)

    db.session.commit()


def load_property_damages():
    """"""

    print("Property Damages")

    PropertyDamage.query.delete()

    for row in open("seed_data/property-damage.txt"):
        row = row.rstrip()
        fema_id, states, counties, damaged_property = row.split("|")

        damaged_property = PropertyDamage(fema_id=fema_id,
                                          damaged_property=damaged_property)

        db.session.add(damaged_property)

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
    load_fema()
    load_property_damages()
