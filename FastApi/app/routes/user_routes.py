"""
This module handles the routes for managing users,
allowing the creation, retrieval, updating, and deletion of user accounts.
"""

import os
from fastapi import APIRouter, Body, HTTPException, Depends
from schemas.user_schema import User
from config.database import UserModel
from helpers.apy_key_auth import get_api_key

user_route = APIRouter()

@user_route.post("/")
async def create_user(user: User = Body(...)):
    """Create a new user."""
    UserModel.create(
        username=user.username,
        email=user.email,
        password_hash=user.password_hash,
        profile_picture=user.profile_picture
    )
    return {"message": "User created successfully"}

@user_route.get("/",dependencies=[Depends(get_api_key)])
async def read_all_users():
    """Retrieve a list of all users."""
    users = UserModel.select().dicts()
    return list(users)

@user_route.get("/{user_id}" , dependencies=[Depends(get_api_key)])
async def read_user(user_id: int):
    """Retrieve a specific user by their ID."""
    try:
        user = UserModel.get(UserModel.id == user_id)
        return user
    except Exception as exc:
        raise HTTPException(status_code=404, detail="User not found") from exc

@user_route.put("/{user_id}" , dependencies=[Depends(get_api_key)])
async def update_user(user_id: int, user: User = Body(...)):
    """Update an existing user's information."""
    try:
        existing_user = UserModel.get(UserModel.id == user_id)
        existing_user.username = user.username
        existing_user.email = user.email
        existing_user.password_hash = user.password_hash
        existing_user.profile_picture = user.profile_picture
        existing_user.save()
        return {"message": "User updated successfully"}
    except Exception as exc:
        raise HTTPException(status_code=404, detail="User not found") from exc

@user_route.delete("/{user_id}", dependencies=[Depends(get_api_key)])
async def delete_user(user_id: int):
    """Delete a user by their ID."""
    rows_deleted = UserModel.delete().where(UserModel.id == user_id).execute()
    if rows_deleted:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@user_route.post("/login", dependencies=None)
async def login(email:str, password_hash:str):
    """Logs in a user by verifying the email and password hash."""
    user = UserModel.get(UserModel.email == email)
    if user:
        if user.password_hash == password_hash:
            return os.getenv("API_KEY")
