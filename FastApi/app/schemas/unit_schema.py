"""Schemas for unit models in the application.

This module defines Pydantic models that represent the structure
and validation for measurement units used in the application.
"""

from pydantic import BaseModel

class Unit(BaseModel):
    """Model representing a unit."""
    id: int
    name: str
