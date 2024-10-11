"""Schemas for user-group relationship models in the application.

This module defines Pydantic models that represent the structure
and validation for relationships between users and groups.
"""

from pydantic import BaseModel

class UserGroup(BaseModel):
    """Model representing a relationship between user and group."""
    id : int
    user_id: int
    group_id: int
