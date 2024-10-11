"""Schemas for the Recipe Ingredient feature in the application.

This module defines Pydantic models that represent the structure
and validation for recipe ingredients within the application.
"""

from pydantic import BaseModel

class RecipeIngredient(BaseModel):
    """Model representing an ingredient in a recipe."""
    id: int
    recipe_id: int
    ingredient_id: int
    quantity: float
    unit_id: int
