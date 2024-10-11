"""Schemas for the Ingredient feature in the application.

This module contains Pydantic models that define the structure
and validation for ingredients within the application.
"""

from pydantic import BaseModel

class Ingredient(BaseModel):
    """Model representing an ingredient."""
    id: int
    name: str
    category_id: int
    unit_id: int
