from typing import List, Union
from pydantic import BaseModel, HttpUrl

class Image(BaseModel):
    url: HttpUrl
    
    class Config:
        orm_mode = True
    
class Price(BaseModel):
    nationality: str
    amount: int
    
    class Config:
        orm_mode = True

class Package(BaseModel):
    offers: str
    
    class Config:
        orm_mode = True

class Location(BaseModel):
    name: str
    city: str
    description: str
    images: Union[List[Image], None] = None
    prices: Union[List[Price], None] = None
    packages: Union[List[Package], None] = None
   
    class Config:
        orm_mode = True

        
class ShowLocation(Location):
    id: int
    
    class Config:
        orm_mode = True
        
        
class ShowImage(Image):
    id: int
    
    class Config:
        orm_mode = True


class ShowPrice(Price):
    id: int
    
    class Config:
        orm_mode = True
        

class ShowPackage(Package):
    id: int
    
    class Config:
        orm_mode = True