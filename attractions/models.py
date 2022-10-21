from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Image(Base):
    __tablename__ = 'images'
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    location_id = Column(Integer, ForeignKey('locations.id'))
    
    location = relationship("Location", back_populates="images")
    
    
class Price(Base):
    __tablename__ = 'prices'
    
    id = Column(Integer, primary_key=True, index=True)
    nationality = Column(String)
    amount = Column(Integer)
    location_id = Column(Integer, ForeignKey('locations.id'))
    
    location = relationship("Location", back_populates="prices")
    
    
    
class Package(Base):
    __tablename__ = 'packages'
    
    id = Column(Integer, primary_key=True, index=True)
    offers = Column(String)
    location_id = Column(Integer, ForeignKey('locations.id'))

    location = relationship("Location", back_populates="packages")
    
    
    
class Location(Base):
    __tablename__ = 'locations'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String)
    description = Column(String)
    
    images = relationship("Image", back_populates="location")
    prices = relationship("Price", back_populates="location")
    packages = relationship("Package", back_populates="location")
   
    