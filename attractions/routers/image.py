from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database


get_db = database.get_db
router = APIRouter(
    tags=['Images']
)



# images
@router.get('/images', response_model=List[schemas.ShowImage], status_code=status.HTTP_200_OK)
async def all_images(db: Session = Depends(get_db)):
    images = db.query(models.Image).all()
    return images

# deleting an image
@router.delete('/images/{image_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_image(image_id: int, db: Session=Depends(get_db)):
    del_image = db.query(models.Image).filter(models.Image.id==image_id)
    
    if del_image.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Image with id {image_id} not found!')
    
    del_image.delete(synchronize_session=False)
    db.commit()
    return f"Location with id {image_id} has been deleted!"
