"""Schemas for recipe type models in the application.

This module defines Pydantic models that represent the structure
and validation for recipe types, including their attributes and relationships.
"""

from pydantic import BaseModel

class RecipeType(BaseModel):
    """Model representing a recipe type."""
    id: int
    name: str
