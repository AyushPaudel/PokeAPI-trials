from fastapi import APIRouter

from core import model
from core import schemas
from services.config import settings
from deps import CURR_USER, DBSession

from sqlalchemy import select


router = APIRouter(
    prefix="/pokemons",
    tags=["Pokemons"]
)

@router.get("/")
async def get_pokemons(curr_user: CURR_USER, db: DBSession, type: str | None = None, name: str | None = None):
    
    if type and name:
        a = select(model.Pokemon).where(model.Pokemon.type.contains([type]) , model.Pokemon.name.contains(name))
        result = (await db.scalars(a)).all()
        return result 
    
    if type: 
        a = select(model.Pokemon).where(model.Pokemon.type.contains([type]))
        result = (await db.scalars(a)).all()

    elif name: 
        a = select(model.Pokemon).where(model.Pokemon.name == name)
        result = (await db.scalars(a)).all()

    else: 
        a = select(model.Pokemon)
        result = (await db.scalars(a)).all()

    return result 
    


