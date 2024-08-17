from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "favorite": [favorite.seralize() for favorite in self.favorites]
        }
    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    user = db.relationship("User", backref='favorites')
    character = db.relationship("Character", backref='favorites')
    planet = db.relationship("Planet", backref="favorites")

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id, 
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    height = db.Column(db.Integer)
    hair_color = db.Column(db.String(20))
    eye_color = db.Column(db.String(20))
    skin_color = db.Column(db.String(20))
    birth_year = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    homeworld = db.Column(db.String(200))
    character_pic = db.Column(db.String(200))

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "character_pic": self.character_pic
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(25))
    gravity = db.Column(db.String(25))

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity
        }
