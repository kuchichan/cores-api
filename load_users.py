from typing import Final, List

from cores_app import models
from cores_app.database import SessionLocal, engine, Base

NAMES: Final[List[str]] = ["Tom", "Jerry", "Donald"]


def main():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)

    for name in NAMES:
        db_user = models.User(name=name)
        db.add(db_user)

    db.commit()
    db.close()


if __name__ == "__main__":
    main()
