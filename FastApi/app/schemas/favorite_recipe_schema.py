"""Schemas for the Favorite Recipe feature in the application.

This module contains Pydantic models that define the structure
and validation for favorite recipes within the user context.
"""

from pydantic import BaseModel

class FavoriteRecipe(BaseModel):
    """Model representing a user's favorite recipe."""
    id: int
    user_id: int
    recipe_id: int
