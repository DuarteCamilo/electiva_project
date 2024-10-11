"""Schemas for the Ingredient Category feature in the application.

This module contains Pydantic models that define the structure
and validation for ingredient categories within the application.
"""

from pydantic import BaseModel

class IngredientCategory(BaseModel):
    """Model representing an ingredient category."""
    id: int
    name: str
