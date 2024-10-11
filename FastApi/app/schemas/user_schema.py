"""Schemas for user models in the application.

This module defines Pydantic models that represent the structure
and validation for user data within the application.
"""

from pydantic import BaseModel

class User(BaseModel):
    """Model representing a user."""
    id: int
    username: str
    email: str
    password_hash: str
    profile_picture: str
