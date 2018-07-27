from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)

from flask_debugtoolbar import DebugToolbarExtension

from model import Event, Location, Type, connect_to_db, connect_to_db

app = Flask(__name__)

app.secret_key = ""

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage"""

    return render_template('homepage.html')


# @app.route('')
