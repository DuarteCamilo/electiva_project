"""Main application module for the FastAPI application.

This module initializes the FastAPI application, sets up the database 
connection lifecycle management, and defines the root endpoint.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from config.database import database as connection
from routes.user_routes import user_route
from routes.group_routes import group_route
from routes.ingredient_category_routes import ingredient_category_route
from routes.unit_routes import unit_route
from routes.recipe_type_routes import recipe_type_route
from routes.recipe_routes import recipe_route
from routes.recipe_recipe_type_routes import recipe_recipe_type_route
from routes.ingredient_routes import ingredient_route
from routes.recipe_ingredient_routes import recipe_ingredient_route
from routes.notification_routes import notification_route
from routes.favorite_recipe_routes import favorite_recipe_route
from routes.menu_routes import menu_route
from routes.menu_recipe_routes import menu_recipe_route
from routes.pantry_item_routes import pantry_item_route
from routes.shopping_list_routes import shopping_list_route
from routes.shopping_list_item_routes import shopping_list_item_route
from routes.user_group_routes import user_group_route

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


app.include_router(user_route, prefix="/api/users", tags=["users"])
app.include_router(group_route, prefix="/api/groups", tags=["groups"])
app.include_router(ingredient_category_route, prefix="/api/ingredient_categories", tags=["ingredient_categories"])
app.include_router(unit_route, prefix="/api/units", tags=["units"])
app.include_router(ingredient_route, prefix="/api/ingredients", tags=["ingredients"])
app.include_router(recipe_type_route, prefix="/api/recipe_types", tags=["recipe_types"])
app.include_router(recipe_route, prefix="/api/recipes", tags=["recipes"])
app.include_router(recipe_recipe_type_route, prefix="/api/recipe_recipe_types", tags=["recipe_recipe_types"])
app.include_router(user_group_route, prefix="/api/user_groups", tags=["user_groups"])
app.include_router(recipe_ingredient_route, prefix="/api/recipe_ingredients", tags=["recipe_ingredients"])
app.include_router(notification_route, prefix="/api/notifications", tags=["notifications"])
app.include_router(favorite_recipe_route, prefix="/api/favorite_recipes", tags=["favorite_recipes"])
app.include_router(menu_route, prefix="/api/menus", tags=["menus"])
app.include_router(menu_recipe_route, prefix="/api/menu_recipes", tags=["menu_recipes"])
app.include_router(pantry_item_route, prefix="/api/pantry_items", tags=["pantry_items"])
app.include_router(shopping_list_route, prefix="/api/shopping_lists", tags=["shopping_lists"])
app.include_router(shopping_list_item_route, prefix="/api/shopping_list_items", tags=["shopping_list_items"])
