"""Schemas for the Recipe-Recipe Type relationship in the application.

This module defines Pydantic models that represent the structure
and validation for the relationship between recipes and their types.
"""

from pydantic import BaseModel

class RecipeRecipeType(BaseModel):
    """Model representing a relationship between recipe and recipe type."""
    id : int
    recipe_id: int
    type_id: int
