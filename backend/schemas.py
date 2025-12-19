from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class UsersBase(BaseModel):
    name: str
    description: Optional[str] = None

class UsersCreate(UsersBase):
    pass

class UsersResponse(UsersBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class HotelsBase(BaseModel):
    name: str
    description: Optional[str] = None

class HotelsCreate(HotelsBase):
    pass

class HotelsResponse(HotelsBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class BookingsBase(BaseModel):
    name: str
    description: Optional[str] = None

class BookingsCreate(BookingsBase):
    pass

class BookingsResponse(BookingsBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DataBase(BaseModel):
    name: str
    description: Optional[str] = None

class DataCreate(DataBase):
    pass

class DataResponse(DataBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class SuiBase(BaseModel):
    name: str
    description: Optional[str] = None

class SuiCreate(SuiBase):
    pass

class SuiResponse(SuiBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DatabaseBase(BaseModel):
    name: str
    description: Optional[str] = None

class DatabaseCreate(DatabaseBase):
    pass

class DatabaseResponse(DatabaseBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class CreateBase(BaseModel):
    name: str
    description: Optional[str] = None

class CreateCreate(CreateBase):
    pass

class CreateResponse(CreateBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

