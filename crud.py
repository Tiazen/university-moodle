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