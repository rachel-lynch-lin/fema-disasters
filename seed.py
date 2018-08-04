"""File to seed the tables created in model.py from the files in seed_data/"""

from sqlalchemy import func
from model import Event, Type
from model import connect_to_db, db

from datetime import datetime
from server import app


def load_events():
    """Load events from event.txt file into the database"""

    print("Events")

    # Delete rows in the table to prevent duplicates if run twice
    Event.query.delete()

    # Read event.txt, organize data, and insert data
    for row in open("seed_data/event.txt"):
        row = row.rstrip().replace("\t", "").split("|")
        # Add list comprehension here in a later version of this file
        for index, value in enumerate(row):
            if value == "":
                row[index] = None

        # row = [None for value in row if value == ""]

        fema_id, state_id, state, county, name, date_range, declared_on, year_declared, month_declared, damaged_property, pa_grant_total = row
        
        name = name.lower()
        name = f"{state} {name}".title()

        events = Event(fema_id=fema_id,
                       state_id=state_id,
                       state=state,
                       county=county,
                       name=name,
                       date_range=date_range,
                       declared_on=declared_on,
                       year_declared=year_declared,
                       month_declared=month_declared,
                       damaged_property=damaged_property,
                       pa_grant_total=pa_grant_total)

        # Add event to the session to be stored
        db.session.add(events)

    # Commit changes
    db.session.commit()


def load_types():
    """Load types from the type.txt file into the database"""

    print("Types")

    Type.query.delete()

    for row in open("seed_data/type.txt"):
        row = row.rstrip().replace("\t", "").split("|")
        fema_id, type_name = row

        types = Type(fema_id=fema_id,
                     type_name=type_name)

        db.session.add(types)

    db.session.commit()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
    db.create_all()
    # Import different types of data
    load_events()
    load_types()
