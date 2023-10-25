from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_teacher = Column(Boolean, default=False)
    
    courses = relationship("Course", back_populates="manager")
    

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    is_active = Column(Boolean, default=False)
    manager_id = Column(Integer, ForeignKey('users.id'))
    
    manager = relationship("User", back_populates="courses")
    course_records = relationship('CourseRecord', back_populates='course')


class CourseRecord(Base):
    __tablename__ = "course_records"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    is_active = Column(Boolean, default=False)
    
    course_id = Column(Integer, ForeignKey('courses.id'))
    
    course = relationship('Course', back_populates='course_records')
    
    