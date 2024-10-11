"""Schemas for the Menu feature in the application.

This module contains Pydantic models that define the structure
and validation for menus in the application.
"""

from pydantic import BaseModel

class Menu(BaseModel):
    """Model representing a menu."""
    id: int
    name: str
    user_id: int
    start_date: str
    end_date: str
