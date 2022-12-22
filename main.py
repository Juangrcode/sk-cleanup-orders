# FastAPI
from fastapi import FastAPI

# Database
from config.db import Base, engine

# Routes
from routes.orders import order


# Create tables for DB
def create_table():
    Base.metadata.create_all(bind=engine)


create_table()


# Create the FastAPI app
app = FastAPI()

# Routes
app.include_router(order)
