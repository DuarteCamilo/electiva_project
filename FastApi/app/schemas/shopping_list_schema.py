"""Schemas for shopping list models in the application.

This module defines Pydantic models that represent the structure
and validation for shopping lists and their attributes.
"""

from pydantic import BaseModel

class ShoppingList(BaseModel):
    """Model representing a shopping list."""
    id: int
    name: str
    created_at: str
    user_id: int
