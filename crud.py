from sqlalchemy.orm import Session
import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    password = user.password + "1234"
    db_user = models.User(email=user.email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_course(db: Session, id: int):
    return db.query(models.Course).filter(models.Course.id == id).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


def create_course(db: Session, course: schemas.CourseCreate, manager: schemas.User):
    db_course = models.Course(
        name=course.name,
        description=course.description,
        is_active=True,
        manager=manager
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def create_course_record(db: Session, record: schemas.CourseRecord, course: schemas.Course):
    db_record = models.CourseRecord(
        name=record.name,
        description=record.description,
        course=course
    )
    
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    
    return db_record
