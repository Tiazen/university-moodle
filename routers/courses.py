from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
import schemas
import crud


router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
    responses={404: {'description': 'Not found'}}
)


@router.get("/", response_model=list[schemas.Course])
def get_all_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@router.get("/{course_id}", response_model=schemas.Course)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course(db=db, id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Сourse not found")
    return course

@router.post("/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    manager = crud.get_user(db=db, user_id=course.manager)
    
    if not manager:
        raise HTTPException(status_code=400, detail="Bad request")
    
    return crud.create_course(db=db, course=course, manager=manager)


@router.post('/{course_id}/record')
def add_record_to_course(course_id: int, course_record: schemas.CourseRecord, db: Session = Depends(get_db)):
    course = crud.get_course(db=db, id=course_id)
    
    if not course:
        raise HTTPException(status_code=404, detail="Сourse not found")
    
    return crud.create_course_record(db=db, record=course_record, course=course)
    
    
    