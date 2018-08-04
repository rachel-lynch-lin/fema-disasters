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

    state_id = db.Column(db.String)

    state = db.Column(db.String)

    county = db.Column(db.String)

    name = db.Column(db.String)

    date_range = db.Column(db.String, default="Unknown")

    declared_on = db.Column(db.DateTime, nullable=False)

    year_declared = db.Column(db.String)

    month_declared = db.Column(db.String)

    damaged_property = db.Column(db.String, default="Unknown")

    pa_grant_total = db.Column(db.String, default="Award amount not listed.")

    user_id = db.Column(db.ForeignKey('users.id'))

    type_id = db.Column(db.ForeignKey('types.id'))

    def __repr__(self):
        """Display info about the disaster event"""

        return f"""<Event ID: {self.id}
                   FEMA ID: {self.fema_id}
                   Location: {self.state_id} {self.state}
                   County Name:{self.county}
                   Name: {self.name}
                   Occured On: {self.date_range}
                   Declared On: {self.declared_on}
                   Year Declared: {self.year_declared}
                   Month Declared: {self.month_declared}
                   Damaged Property: {self.damaged_property}
                   Public Assistance Total Grant: ${self.pa_grant_total}>"""


class Type(db.Model):
    """Types of disasters that have occured in California"""

    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    type_name = db.Column(db.String)  # Take from type_name

    def __repr__(self):
        """Display type of disaster"""

        return f"""<Type ID: {self.id}
                   Type Name: {self.type_name}>"""


class User(db.Model):
    """Keep user info to save user info"""

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


class UserSearch(db.Model):
    """Joining the event and location"""

    __tablename__ = "user_searches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    users_id = db.Column(db.ForeignKey('users.id'))

    events_id = db.Column(db.ForeignKey('events.id'))

    def __repr__(self):
        """Display type of disaster"""

        return f"""<User-Searches ID: {self.id}
                   User ID: {self.users_id}
                   Event ID:{self.events_id}>"""


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
