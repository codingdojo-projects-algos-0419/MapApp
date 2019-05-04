import os
from flask import render_template, request, redirect, session, url_for
from config import db, app
from server.models.locations import Location
from server.models.users import User



def view_location(location_id):
        location = Location.query.get(location_id)
        if 'user_id' in session:
                user = User.query.get(session['user_id'])
                return render_template('location.html', user=user, location=location)
        return render_template('location.html', location=location)


def like(location_id):
        user = User.query.get(session['user_id'])
        location = Location.query.get(location_id)
        location.users_who_like_this_location.append(user)
        db.session.commit()
        return redirect(url_for('users:account_page', user_id=user.id))

def remove_like(location_id):
        user = User.query.get(session['user_id'])
        location = Location.query.get(location_id)
        location.users_who_like_this_location.remove(user)
        db.session.commit()
        return redirect(url_for('locations:view_location', location_id=location_id))


def add_destination():
        if 'user_id' in session:
                destination = Location(user_id=session['user_id'], address=request.form['destination'])
                db.session.add(destination)
                db.session.commit()
        return redirect(url_for('dashboard'))