"""Schemas for recipe models in the application.

This module defines Pydantic models that represent the structure
and validation for recipes, including their attributes and relationships.
"""

from pydantic import BaseModel

class Recipe(BaseModel):
    """Model representing a recipe."""
    id: int
    name: str
    description: str
    instructions: str
    preparation_time: int
    datosNutricionales: str
    type_id: int
    difficulty: str
    is_public: bool
    user_id: int
