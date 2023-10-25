from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str
    description: str


class Course(CourseBase):
    id: int
    

class CourseRecords:
    id: int
    name: str
    description: str
    
    course: Course

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_teacher: bool