from typing import Optional

from pydantic import BaseModel


class Core(BaseModel):
    id: str
    reuse_count: int
    total_mass: int

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    name: str
    favourite_core: Optional[Core]

    class Config:
        orm_mode = True


class UserCoreUpdate(BaseModel):
    favourite_core_id: Optional[str]
