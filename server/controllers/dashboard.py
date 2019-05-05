from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import desc
from config import db
from server.models.users import User
from server.models.locations import Location

def dashboard():
    locations = Location.query.all()
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if 'destination' in session:
            destination = session['destination']
            session.pop('destination')
        else:
            destination = ""
        print(destination)
        return render_template('dashboard.html', user=user, destination=destination)

    return render_template('dashboard.html')
