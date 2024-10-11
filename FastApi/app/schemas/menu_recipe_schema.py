"""Schemas for the Menu Recipe feature in the application.

This module contains Pydantic models that define the structure
and validation for recipes associated with menus in the application.
"""

from pydantic import BaseModel

class MenuRecipe(BaseModel):
    """Model representing a recipe in a menu."""
    id: int
    menu_id: int
    recipe_id: int
    meal_time: str
    planned_date: str
