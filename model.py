"""Models and database functions for California Disaster project"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy

###############################################################################
# Model definitions
# types = [coastal_storm, dam_levee_break, drought, earthquake, fire,
#          fishing_losses, flood, freeze, other, severe_storm, tsunami,
#          wildfire]
# type_name = ["Coastal Storm", "Dam/Levee Break", "Drought", "Earthquake",
#              "Fire", "Fishing Losses", "Flood", "Freeze", "Other",
#              "Severe Storm", "Tsunami", "Wildfire"]


class Type(db.Model):
    """Types of disasters that have occured in California"""

    __tablename__ = "types"

    type_id = db.Column(db.String(25), primary_key=True)  # Take from types

    type_name = db.Column(db.String(25))  # Take from type_name

    def __repr__(self):
        """Display type of disaster"""

        return f"{self.type_name}"
