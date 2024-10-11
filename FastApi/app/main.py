"""Main application module for the FastAPI application.

This module initializes the FastAPI application, sets up the database 
connection lifecycle management, and defines the root endpoint.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from config.database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage the lifespan of the FastAPI application.

    This function establishes a database connection when the application starts
    and ensures that the connection is closed when the application stops.
    """
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    """Redirect the root URL to the API documentation."""
    return RedirectResponse(url="/docs")
