"""File to seed the tables created in model.py from the files in seed_data/"""

from sqlalchemy import func
from model import Event, Grant
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

        declaration_id, fema_id, state_id, state, name, county, start_date, end_date, declared_on, close_out_date,  disaster_type = row

<<<<<<< HEAD
        name = name.lower()

        name = f"{state} {name}".title()

        declared_on = declared_on[:-14]

        events = Event(fema_id=fema_id,
=======
        name = name.lower().title()
        name = f"{state_id} {name}"

        events = Event(declaration_id=declaration_id,
                       fema_id=fema_id,
                       state_id=state_id,
>>>>>>> 0714e6ef584c6adfa635210d75c78d3c33e15bd5
                       state=state,
                       name=name,
                       county=county,
                       start_date=start_date,
                       end_date=end_date,
                       declared_on=declared_on,
                       close_out_date=close_out_date,
                       disaster_type=disaster_type)

        # Add event to the session to be stored
        db.session.add(events)

    # Commit changes
    db.session.commit()


def load_grants():
    """Load grants from the grant.txt file into the database"""

    print("Grants")

<<<<<<< HEAD
    for row in open("seed_data/location.txt"):
        row = row.rstrip().split("|")
        state_id, state, county = row
=======
    Grant.query.delete()
>>>>>>> 0714e6ef584c6adfa635210d75c78d3c33e15bd5

    for row in open("seed_data/grant.txt"):
        row = row.rstrip().replace("\t", "").split("|")
        print(row[0])
        events = Event.query.filter_by(fema_id=row[0]).all()
        for event in events:
            type_names = {0: "FEMA ID",
                          1: "Total Public Assistance Grants (PA)",
                          2: "Emergency Work(Categories A-B)",
                          3: "Permanent Work (Categories C-G)",
                          4: "Total Individual & Households Program (IHP)",
                          5: "Total Individual Assistance (IA) Applications",
                          6: "Total Housing Assistance (HA)",
                          7: "Total Other Needs Assistance (ONA)"}

            for index, value in enumerate(row):
                if index > 0 and index < 8 and value != "":
                    event.grants.append(Grant(total=value, grant_type=type_names[index]))

    db.session.commit()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
    db.create_all()
    load_events()
    load_grants()
