from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr
    city: str
    interests: List[str]

    @validator('gender')
    def validate_gender(cls, value):
        if value not in {"male", "female", "other"}:
            raise ValueError("Gender must be 'male', 'female', or 'other'")
        return value

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    email: Optional[EmailStr]
    city: Optional[str]
    interests: Optional[List[str]]

    @validator('gender')
    def validate_gender(cls, value):
        if value and value not in {"male", "female", "other"}:
            raise ValueError("Gender must be 'male', 'female', or 'other'")
        return value

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
