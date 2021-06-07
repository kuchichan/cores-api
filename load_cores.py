import asyncio

from rocket_cores.fetch_data import fetch_data_automatically

from cores_app import models
from cores_app.database import SessionLocal, engine, Base


async def fetch_cores():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)

    cores_data = await fetch_data_automatically(
        only_successful=False, future_launches=True, limit=0
    )

    for core_id, reuse_count, total_mass in cores_data:
        db_core = models.Core(
            id=core_id, reuse_count=reuse_count, total_mass=total_mass
        )
        db.add(db_core)

    db.commit()
    db.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_cores())
