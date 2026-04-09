from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '3f8a2c9b1e7d4f3a5b6c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9'
db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    login = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    task = db.relationship('Task', backref='worker', uselist=False)
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    
    worker_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    
    
with app.app_context():
    db.create_all()
    existing_admin = Admin.query.filter_by(login='admin').first()
    if not existing_admin:
        admin = Admin(
            login='admin',
            password=generate_password_hash('admin123')
        )
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)