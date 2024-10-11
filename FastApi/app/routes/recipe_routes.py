"""
This module handles the routes for managing recipes, 
allowing users to create, retrieve, update, and delete recipes.
"""

from fastapi import APIRouter, Body, HTTPException
from schemas.recipe_schema import Recipe
from config.database import RecipeModel

recipe_route = APIRouter()

@recipe_route.post("/")
async def create_recipe(recipe: Recipe = Body(...)):
    """Create a new recipe."""
    RecipeModel.create(
        name=recipe.name,
        description=recipe.description,
        instructions=recipe.instructions,
        preparation_time=recipe.preparation_time,
        datosNutricionales=recipe.datosNutricionales,
        type_id=recipe.type_id,
        difficulty=recipe.difficulty,
        is_public=recipe.is_public,
        user_id=recipe.user_id
    )
    return {"message": "Recipe created successfully"}

@recipe_route.get("/")
async def read_all_recipes():
    """Retrieve a list of all recipes."""
    recipes = RecipeModel.select().dicts()
    return list(recipes)

@recipe_route.get("/{recipe_id}")
async def read_recipe(recipe_id: int):
    """Retrieve a specific recipe by its ID."""
    try:
        recipe = RecipeModel.get(RecipeModel.id == recipe_id)
        return recipe
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Recipe not found") from exc

@recipe_route.put("/{recipe_id}")
async def update_recipe(recipe_id: int, recipe: Recipe = Body(...)):
    """Update an existing recipe."""
    try:
        existing_recipe = RecipeModel.get(RecipeModel.id == recipe_id)
        existing_recipe.name = recipe.name
        existing_recipe.description = recipe.description
        existing_recipe.instructions = recipe.instructions
        existing_recipe.preparation_time = recipe.preparation_time
        existing_recipe.datosNutricionales = recipe.datosNutricionales
        existing_recipe.type_id = recipe.type_id
        existing_recipe.difficulty = recipe.difficulty
        existing_recipe.is_public = recipe.is_public
        existing_recipe.user_id = recipe.user_id
        existing_recipe.save()
        return {"message": "Recipe updated successfully"}
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Recipe not updated") from exc
