"""Schemas for the Group feature in the application.

This module contains Pydantic models that define the structure
and validation for user groups within the application.
"""

from pydantic import BaseModel

class Group(BaseModel):
    """Model representing a user group."""
    id: int
    name: str
