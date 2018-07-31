from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask import jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import Event, Location, Type, User, UserSearch, LocationEvent

from model import connect_to_db, db

import os

app = Flask(__name__)

app.secret_key = "SERVER_APP_SECRET_KEY"
google_api_key = os.environ["GOOGLE_API_KEY"]

app.jinja_env.undefined = StrictUndefined

###############################################################################


@app.route('/')
def index():
    """Homepage"""

    return render_template('homepage.html', google_api_key=google_api_key)


@app.route('/users')
def show_users():
    """Show a list of all users"""

    users = User.query

    return render_template('users-list.html',
                           users=users)


@app.route('/users/<int:user_id>')
def show_user_page(user_id):
    """Show user info page with saved queries"""

    user = User.query.get(user_id)

    if not user:
        flash('User does not exist')
        return redirect('/login')

    user_saved_searches = db.session.query(UserSearch.id,
                                           UserSearch.users_id,
                                           UserSearch.events_id
                                           ).join(
                                                Event
                                           ).filter_by(
                                                user_id=user_id
                                           ).all()

    return render_template('user-info.html',
                           user=user,
                           user_saved_searches=user_saved_searches)


@app.route('/registration')
def show_registration_form():
    """Show registration form"""

    return render_template('registration.html')


@app.route('/registration', methods=['POST'])
def register_user():
    """Register a new user after checking db to make sure it does not exist"""
    print(request.form)
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    occupation = request.form.get('occupation')
    user = User.query.filter_by(username=username).first()
    user_email = User.query.filter_by(email=email).first()

    if user:
        flash('Username is taken')
        return redirect('/registration')

    if user_email:
        flash('Email is already in use')
        return redirect('/registration')

    new_user = User(username=username,
                    email=email,
                    password=password,
                    occupation=occupation)
    db.session.add(new_user)
    db.session.commit()

    flash("New User Registration Complete")

    return redirect('/login')


@app.route('/login')
def show_login_form():
    """Show login form"""

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def process_login():
    """Complete login process"""

    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        flash('Invalid password')
        return redirect('/login')

    session['user_id'] = user.id

    flash("Logged In")

    return redirect(f'/users/{user.id}')


@app.route('/logout')
def process_logout():
    """User logout and provide message upon success"""

    session.pop('user_id')
    flash('Logout Successful')

    return redirect('/')


@app.route('/events')
def events_list():
    """Show events list ordered by date"""

    events = Event.query.order_by('start_date').all()

    return render_template('event-list.html',
                           events_list=events)


@app.route('/events/<int:fema_id>')
def show_user_events_info(fema_id):
    """Find an event"""

    event = Event.query.get(fema_id)

    if not event:
        flash('This event does not exist or this datebase is incomplete.')
        return redirect('/')

    return render_template('event-info.html',
                           event=event)


@app.route('/types.json')
def types_list():
    """Display a list of disaster types"""

    types = {
        types.id: {
            "Type ID": types.id,
            "Type Name": types.type_name
        }
        for types in Type.query}

    return jsonify(types)


@app.route('/type/<user_type>')
def show_user_type(user_type):
    """Display all events with that type"""

    user_type = Type.query.get(id)

    if not user_type:
        flash('This type does not exist in this datebase.')
        return redirect('/')

    return render_template('type-info.html',
                           user_type=user_type)


@app.route('/locations/<user_state>')
def show_ulocation_by_state(user_state):
    """Show user queried location by state selected"""

    state = Location.query.get(user_state)

    if not state:
        flash('This is not a state in the United States.')
        return redirect('/')

    return render_template('user-state.html',
                           state=state)


@app.route('/locations/<user_county>')
def show_ulocation_by_county(user_county):
    """Show user queried location by county selected via zipcode/city"""

    county = Location.query.get(user_county)

    if not county:
        flash('This is not a county is not in this datebase')
        return redirect('/')

    return render_template('user-county.html',
                           county=county)


@app.route('/about')
def show_about_page():
    """Show the about page"""

    return render_template('about.html')


@app.route('/contact')
def show_contact_page():
    """Show contact page"""

    return render_template('contact.html')


@app.route('/us-map')
def us_map():
    """Show a map of the entire United States without markers"""

    return render_template('us-map.html', google_api_key=google_api_key)


@app.route('/geolocate')
def geolocate():
    """Zoom in on the location queried by the user with markers"""

    return render_template('geolocate.html', google_api_key=google_api_key)


###############################################################################


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
