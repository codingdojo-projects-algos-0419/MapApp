from sqlalchemy.sql import func
from flask import session
from config import db
from server.models.likes_table import likes_table

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False
    )
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )
    user=db.relationship(
        'User', foreign_keys=[user_id], backref=db.backref(
            "locations", cascade="all, delete-orphan"
            )
    )
    users_who_like_this_location = db.relationship('User', secondary=likes_table, cascade='all')

    def not_liked(self):
        user = User.query.get(session['user_id'])
        if user in self.user_who_like_this_post:
            return False
        else:
            return True

    def likes(self):
        likes = 0 
        likes_users = self.users_who_like_this_location
        for user in likes_users:
            likes += 1
        return likes

    @classmethod
    def validate(cls, form):
        errors = []
        existing_location = cls.query.filter_by(address=form['destination']).filter_by(user_id=session['user_id']).first()
        if existing_location:
            errors.append("Address already saved.")
        if len(form['destination']) > 255:
            errors.append("Name cannot exceed 255 characters in length.")
        if len(form['destination']) <= 4:
            errors.append("Name mush consist of at least 4 characters.")
        return errors

    @classmethod
    def create(cls, form, user_id):
        post = cls(title=form['name'], user_id=user_id)
        db.session.add(post)
        db.session.commit()
