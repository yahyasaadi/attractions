from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database


get_db = database.get_db
router = APIRouter(
    tags=['Locations']
)

# Adding a location
@router.post('/locations', response_model=schemas.Location, status_code=status.HTTP_201_CREATED)
async def create(location: schemas.Location, db: Session = Depends(get_db)):
    location_data = location.dict()
    
    images_data = location_data.pop("images")
    prices_data = location_data.pop("prices")
    packages_data = location_data.pop("packages")

    new_location = models.Location(**location_data)
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    
    location_id = new_location.id
    
    # add images
    for img in images_data:
        img['location_id'] = location_id
        db_image = models.Image(**img)
        db.add(db_image)
        db.commit()
        db.refresh(db_image)
        
    # add prices
    for price in prices_data:
        price['location_id'] = location_id
        db_price = models.Price(**price)
        db.add(db_price)
        db.commit()
        db.refresh(db_price)
    
    # add packages
    for package in packages_data:
        package['location_id'] = location_id
        db_package = models.Package(**package)
        db.add(db_package)
        db.commit()
        db.refresh(db_package)
        
    return new_location


# Querying all Locations
@router.get('/locations', response_model=List[schemas.ShowLocation], status_code=status.HTTP_200_OK)
async def all_locations(db: Session = Depends(get_db)):
    locations = db.query(models.Location).all()
    return locations


# Getting a location by id
@router.get('/locations/{loc_id}', response_model=schemas.ShowLocation, status_code=status.HTTP_200_OK)
async def location_by_id(loc_id: int, db: Session=Depends(get_db)):
    location = db.query(models.Location).filter(models.Location.id == loc_id).first()
    
    if location is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Locations with id {loc_id} not found.")
    return location

# Updating a location by id
@router.put('/locations/{loc_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_location(loc_id: int, location: schemas.Location, db: Session=Depends(get_db)):
    location_update = db.query(models.Location).filter(models.Location.id==loc_id)
    
    if location_update.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Locations with id {loc_id} not found.")
        
    location_update.update({"name":location.name, "city":location.city, "description":location.description})
    db.commit()
    return f"Location with id {loc_id} successfully updated!"


# Deleting a location
@router.delete('/locations/{loc_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_location(loc_id: int, db: Session=Depends(get_db)):
    del_location = db.query(models.Location).filter(models.Location.id==loc_id)
    
    if del_location.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Locations with id {loc_id} not found.")
        
    del_location.delete(synchronize_session=False)
    db.commit()
    return f"Location with id {loc_id} has been deleted!"


# Filter location by city
@router.get('/locations/city_name/{city}', response_model=List[schemas.ShowLocation], status_code=status.HTTP_200_OK)
async def filter_by_location(city: str, db: Session=Depends(get_db)):
    locations = db.query(models.Location).filter(models.Location.city==city.title()).all()
    
    if len(locations)==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Locations with city of {city} not found.")
    return locations

