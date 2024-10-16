"""Schemas for the Pantry Item feature in the application.

This module defines Pydantic models that represent the structure
and validation for pantry items within the application.
"""

from pydantic import BaseModel

class PantryItem(BaseModel):
    """Model representing an item in the pantry."""
    id: int
    quantity: float
    unit: str
    expiry_date: str
    user_id: int
    ingredient_id: int
