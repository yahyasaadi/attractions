from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database


get_db = database.get_db
router = APIRouter(
    tags=['Prices']
)

# prices
@router.get('/prices', response_model=List[schemas.ShowPrice], status_code=status.HTTP_200_OK)
async def all_prices(db: Session = Depends(get_db)):
    prices = db.query(models.Price).all()
    return prices

# deleting an image
@router.delete('/prices/{price_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_image(price_id: int, db: Session=Depends(get_db)):
    del_price = db.query(models.Price).filter(models.Price.id==price_id)
    
    if del_price.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Image with id {price_id} not found!')
    
    del_price.delete(synchronize_session=False)
    db.commit()
    return f"Location with id {price_id} has been deleted!"

