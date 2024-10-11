"""Schemas for shopping list item models in the application.

This module defines Pydantic models that represent the structure
and validation for items in a shopping list, including their attributes
and relationships to other entities.
"""

from pydantic import BaseModel

class ShoppingListItem(BaseModel):
    """Model representing an item in a shopping list."""
    id: int
    shopping_list_id: int
    ingredient_id: int
    quantity: float
    unit: str
    is_purchased: bool
