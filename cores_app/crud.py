from sqlalchemy.orm import Session
from rocket_cores.fetch_data import fetch_data_automatically
from . import models, schemas


async def get_cores(db: Session, offset: int = 0, limit: int = 10):
    cores_db = db.query(models.Core).offset(offset).limit(limit).all()
    if not cores_db:
        result = await fetch_data_automatically(
            only_successful=False,
            future_launches=True,
            limit=0,
            offset=offset,
        )  # To be discussed - pagination for api looks weird
        for core_id, reuse_count, total_mass in result:
            db.add(
                models.Core(id=core_id, reuse_count=reuse_count, total_mass=total_mass)
            )
        db.commit()

    cores_db = db.query(models.Core).offset(offset).limit(limit).all()
    return cores_db


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def update_user_favourite_core(
    db: Session, user_id: int, user_core_update: schemas.UserCoreUpdate
):

    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    fav_core_id = user_core_update.favourite_core_id
    db_core = db.query(models.Core).filter(models.Core.id == fav_core_id).first()
    if db_core is None:
        return None
    db_user.favourite_core_id = fav_core_id
    db.commit()
    db.refresh(db_user)
    return db_user
