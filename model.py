"""Models and database functions for California Disaster project"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

###############################################################################
# Model definitions


class Event(db.Model):
    """The disaster declarations that are in FEMA's database"""

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    declaration_id = db.Column(db.String, nullable=False)

    fema_id = db.Column(db.Integer)

    state_id = db.Column(db.String)

    state = db.Column(db.String)

    name = db.Column(db.String)

    county = db.Column(db.String)
<<<<<<< HEAD

    start_date = db.Column(db.DateTime)

    end_date = db.Column(db.DateTime)

    declared_on = db.Column(db.DateTime)

    close_out_date = db.Column(db.DateTime)

    disaster_type = db.Column(db.String)

    grants = db.relationship('Grant', backref='event')

=======

    start_date = db.Column(db.DateTime)

    end_date = db.Column(db.DateTime)

    declared_on = db.Column(db.DateTime)

    close_out_date = db.Column(db.DateTime)

    disaster_type = db.Column(db.String)

    grants = db.relationship('Grant', backref='event')

>>>>>>> 0714e6ef584c6adfa635210d75c78d3c33e15bd5
    damaged_property = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """Display info about the disaster event"""

        return f"""<Event ID: {self.id}
                   Declaration ID: {self.declaration_id}
                   FEMA ID: {self.fema_id}
                   State ID: {self.state_id}
                   State: {self.state}
                   Name: {self.name}
                   County:{self.county}
                   Occured On: {self.start_date} - {self.end_date}
                   Declared On: {self.declared_on}
                   Disaster Closed Out On: {self.close_out_date}
                   Disaster Type: {self.disaster_type}>"""

<<<<<<< HEAD

class Grant(db.Model):
    """Money that was awarded for disasters"""

    __tablename__ = "grants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    total = db.Column(db.Float)

    grant_type = db.Column(db.String)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)


    def __repr__(self):
        """Display information about funding that was granted"""

        return f"""<Grant Total ID: {self.id}
                   Total: {self.total}
                   Grant Type: {self.grant_type}
                   Event ID: {self.event_id}"""
=======

class Grant(db.Model):
    """Money that was awarded for disasters"""

    __tablename__ = "grants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    total = db.Column(db.Float)

    grant_type = db.Column(db.String)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

    # fema_id = db.Column(db.Integer)

    # pa_grant_total = db.Column(db.Float, default=None)  # Change to float later

    # cat_ab_total = db.Column(db.Float, default=None)

    # cat_cg_total = db.Column(db.Float, default=None)

    # ihp_total = db.Column(db.Float, default=None)  # Change to float later

    # ia_apps_approved = db.Column(db.Integer)

    # ha_total = db.Column(db.Float, default=None)

    # ona_total = db.Column(db.Float, default=None)

    def __repr__(self):
        """Display information about funding that was granted"""

        return f"""<Grant Total ID: {self.id}
                   FEMA ID: {self.fema_id}"""
                   # Public Assistance Total Grant: ${self.pa_grant_total}
                   # EM WK(Cats A-B) $'s Obligated: ${self.cat_ab_total}
                   # PM WK(Cats C-G) $'s Obligated: ${self.cat_cg_total}
                   # Total IHP $'s Approved: ${self.ihp_total}
                   # Total IA Applications Approved: {self.ia_apps_approved}
                   # Total HA $'s Approved: ${self.ha_total}
                   # Total ONA $'s Approved: ${self.ona_total}
                   # Damaged Property: {self.damaged_property}>
>>>>>>> 0714e6ef584c6adfa635210d75c78d3c33e15bd5


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
        """Display information about the user's saved searches"""

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
