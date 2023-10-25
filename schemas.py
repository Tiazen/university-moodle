from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_teacher: bool


class BaseRecord(BaseModel):
    id: int


class CourseRecord(BaseRecord):
    name: str
    description: str


class CourseBase(BaseModel):
    name: str
    description: str


class Course(CourseBase):
    id: int
    manager: User
    course_records: List[CourseRecord]
    

class CourseCreate(CourseBase):
    manager: int