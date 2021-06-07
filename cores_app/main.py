from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/cores/", response_model=List[schemas.Core])
async def read_cores(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cores = await crud.get_cores(db, offset, limit)
    return cores


@app.get("/users/{user_id}/", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.patch("/users/{user_id}/like/", response_model=schemas.User)
def like_core(
    user_id: int, update_data: schemas.UserCoreUpdate, db: Session = Depends(get_db)
):
    db_user = crud.update_user_favourite_core(db, user_id, update_data)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found or core id invalid")
    return db_user
