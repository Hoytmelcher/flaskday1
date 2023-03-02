from datetime import datetime
from app import db 
from werkzeug.security import generate_password_hash, check_password_hash

# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(120), nullable=True)
    listings = db.relationship('Listing', backref='seller', lazy='dynamic')

    def __repr__(self):
        return f'<User: {self.username}>'
    
    def __str__(self):
        return f'User: {self.email}|{self.username}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def commit(self):
        db.session.add(self)
        db.session.commit()


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(64))
    model = db.Column(db.String(64))
    year = db.Column(db.Integer)
    color = db.Column(db.String(64))
    price = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.price.data}: {self.color.data} {self.year.data} {self.make.data} {self.model.data}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()