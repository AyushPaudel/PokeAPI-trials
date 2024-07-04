import requests
from services.database import get_db
from core.model import Pokemon
import asyncio

async def get_individual_pokemon(url):
    r = requests.get(url=url)
    poke_data = r.json()
    poke_name = poke_data['name']
    poke_abilities = [ability['ability']['name'] for ability in poke_data['abilities']]
    poke_type = [type_['type']['name'] for type_ in poke_data['types']]
    poke_id = poke_data['id'] 
    poke_img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png"
    new_pokemon = Pokemon(
        name = poke_name,
        ability = poke_abilities, 
        type = poke_type,
        image = poke_img

    )
    await save_in_db(new_pokemon)
    return 


async def save_in_db(new_pokemon):
    async for session in get_db():
        print(dir(session))
        session.add(new_pokemon)
        await session.commit()
        await session.refresh(new_pokemon)
    
    return 


async def main():
    # url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    url ="https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
    r = requests.get(url=url)
    b = r.json()['results']
    for individual in b:
        await get_individual_pokemon(individual['url'])
        pass



    
asyncio.run(main())