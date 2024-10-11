"""
This module handles API authentication using an API key.
"""

import os
from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    """
    Verifies if the provided API key is valid.

    Args:
        api_key (str): The API key provided in the header.

    Returns:
        str: The API key if it is valid.

    Raises:
        HTTPException: If the API key is invalid.
    """

    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "status": False,
                "status_code": status.HTTP_403_FORBIDDEN,
                "message": "Unauthorized",
            },
        )
