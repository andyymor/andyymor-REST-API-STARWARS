from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column,String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    # favorites = relationship("Favorites", back_populates = "user")
    
    def __repr__(self):
        return '<User %r>' % self.username
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "favorites": self.favorite,
            # do not serialize the password, its a security breach
        }
class Favorites(db.Model):
    __tablename__ = "favorite"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"))
    # user = relationship("User", back_populates = "favorites")

   
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
            "planet": self.planet_id,
            "people": self.people_id
            
            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=True)
    diameter = db.Column(db.Integer, unique=False, nullable=True)
    gravity = db.Column(db.Integer, unique=False, nullable=True)
    orbital_period = db.Column(db.Integer, unique=False, nullable=True)
    climate = db.Column(db.String(80), unique=False, nullable=True)
    terrain = db.Column(db.String(80), unique=False, nullable=True)
   
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "climate": self.climate,
            "terrain": self.terrain,
        }
    

class People(db.Model):
    __tablename__= "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=True)
    height = db.Column(db.Integer, unique=False, nullable=True)
    weight = db.Column(db.Integer, unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=True)
    race = db.Column(db.String(80), unique=False, nullable=True)
    hair_color = db.Column(db.String(80), unique=False, nullable=True)
    eye_color = db.Column(db.String(80), unique=False, nullable=True)
    homeworld = db.Column(db.String(250))
    # species_id = db.Column(db.String(250), ForeignKey=("species.id"))
    # species = relationship("Species", back_populates=("people"))

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "age": self.age,
            "race": self.race,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "homeworld": self.homeworld
        } 


class Vehicle(db.Model):
    __tablename__= "vehicle"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(225))
    name = db.Column(db.String(120), unique=True, nullable=False)
    model_name = db.Column(db.String(80))
    manufacturer = db.Column(db.String(100))
    price = db.Column(db.Integer)
    description = db.Column(db.String(500))

    
    def serialize(self):
        return {
    "id":self.id,
    "image_url": self.image_url,
    "name": self.name ,
    "model_name": self.model_name,
    "manufacturer":self.manufacturer,
    "price": self.price,
    "description": self.description

        }














