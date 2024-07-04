from fastapi import APIRouter

from routes import users, pokemon

routers = APIRouter(prefix='/api/v1')

routers.include_router(users.router)
routers.include_router(pokemon.router)