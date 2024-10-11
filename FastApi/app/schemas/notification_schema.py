"""Schemas for the Notification feature in the application.

This module contains Pydantic models that define the structure
and validation for notifications in the application.
"""

from pydantic import BaseModel

class Notification(BaseModel):
    """Model representing a notification."""
    id: int
    user_id: int
    message: str
    created_at: str
    is_read: bool
