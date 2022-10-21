from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database


get_db = database.get_db
router = APIRouter(
    tags=['Packages']
)

# packages
@router.get('/packages', response_model=List[schemas.ShowPackage], status_code=status.HTTP_200_OK)
async def all_packages(db: Session = Depends(get_db)):
    packages = db.query(models.Package).all()
    return packages

# deleting an image
@router.delete('/packages/{package_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_package(package_id: int, db: Session=Depends(get_db)):
    del_package = db.query(models.Package).filter(models.Package.id==package_id)
    
    if del_package.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Image with id {package_id} not found!')
    
    del_package.delete(synchronize_session=False)
    db.commit()
    return f"Location with id {package_id} has been deleted!"