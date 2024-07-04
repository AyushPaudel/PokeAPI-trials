# A FastAPI project that utilizes Poke API to get pokemon name, type, abilities and image

### To run
- change directory to app/ 
- run 
- run: 
  - `python -m venv env`
  - activate env
  - `pip install -r requirements.txt`
  - `alembic alembic revision --autogenerate -m "Creating DB models"`
  - `alembic upgrade head`
  - `python request.py`
  - `uvicorn main:app --reload`
  
