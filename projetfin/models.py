from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY
from flask_sqlalchemy import SQLAlchemy



#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
db = SQLAlchemy()


#Table association : Relation one to many
class Show(db.Model):
    __tablename__ = 'show'

    id = db.Column(db.Integer, primary_key=True)
    #https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id', ondelete='CASCADE'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

    #https://newbedev.com/sqlalchemy-default-datetime
    start_time = db.Column('start_time', db.DateTime, server_default=func.now(), nullable=False)

def __repr__(self):
    return f'<Show {self.id} {self.start_time}>'

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    #https://stackoverflow.com/questions/59362348/reading-character-array-instead-of-string-array-from-flask-sqlalchemy
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean,  default=False)
    seeking_description = db.Column(db.String())
    #https://docs.sqlalchemy.org/en/14/orm/cascades.html#passive-deletes
    show = db.relationship('Show', backref='venue', lazy=True, cascade="all, delete",passive_deletes=True,)

def __repr__(self):
    return f'<Venue {self.id} {self.name}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venues = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String())
    
    #Relation
    show = db.relationship('Show', backref='artist', lazy=True)

def __repr__(self):
    return f'<Artist {self.id} {self.name}>'

  