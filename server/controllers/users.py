from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import func
from app import db
from server.models.locations import Location
from server.models.users import User

def login_and_registration():
    return render_template('Log_and_reg.html')

def create():
    errors = User.validate(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('users:login_and_registration'))
    user_id = User.create(request.form)
    session['user_id'] = user_id
    return redirect(url_for("dashboard"))

def login():
    valid, response = User.login_helper(request.form)
    if not valid:
        flash(response)
        return redirect(url_for("users:login_and_registration"))
    session['user_id'] = response
    return redirect(url_for("dashboard"))

def logout():
    session.clear()
    return redirect(url_for("dashboard"))

def account_page(user_id):
    current_user = User.query.get(session['user_id'])
    user = User.query.get(user_id)
    if current_user.id == user.id:
        return render_template('account_page.html', current_user=current_user, user=user)
    return redirect(url_for('dashboard'))

def editing(user_id):
    user = User.query.get(user_id)
    errors = User.edit_validate(request.form)
    if errors:
        for error in errors:
                flash(error)
        return redirect(url_for('users:edit'))
    user.username = request.form['username']
    db.session.commit()
    return redirect(url_for('dashboard'))
