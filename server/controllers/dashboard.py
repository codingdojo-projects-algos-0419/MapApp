from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import desc
from config import db
from server.models.users import User
from server.models.locations import Location

def dashboard():
    locations = Location.query.all()
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user)
    return render_template('dashboard.html')
