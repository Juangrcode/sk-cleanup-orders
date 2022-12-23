# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


# Cors
origins = [
    "https://sk-cleanup-web-app.vercel.app",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
app.include_router(order)
