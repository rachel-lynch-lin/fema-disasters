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
    for row in open("seed_data/event.txt")
