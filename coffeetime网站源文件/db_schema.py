from flask import Flask                     # Import the Flask module from the flask package
from flask_sqlalchemy import SQLAlchemy     # Import the SQLAlchemy module from the flask_sqlalchemy package

app = Flask(__name__)                                               # Declare that this is a Flask app
db = SQLAlchemy(app)                                                # Initialize the SQLAlchemy flask database object
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///user.db'   # Setup the database file "crud_demo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                # Disable modification track
app.config['SECRET_KEY'] = 'mysecretkey'                            # Initialize SECRET_KEY used to encrypt your cookies 
                                                                    # and save send them to the browser for session management.

class User(db.Model):                                               # Define User table class and call it 'users'
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # Define primary key id.
    username = db.Column(db.String(50))                              # Define other fields. 
    email = db.Column(db.String(255))
    password = db.Column(db.String(80))
    bio = db.Column(db.String(300))
    admin = db.Column(db.Boolean)
    image_file = db.Column(db.String(255), nullable=False, default='default.jpg')
    active = db.Column(db.Boolean)