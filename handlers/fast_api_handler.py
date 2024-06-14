from typing import List, Dict, Any
from fastapi import FastAPI, Form, Depends, HTTPException, status
from fastapi import APIRouter
from icecream import ic
from starlette.responses import FileResponse

from models.users import User
from shemas.user import UserOut, UserFilePath

router = APIRouter(
    prefix="",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/users/", response_model=List[UserOut])
async def all_user() -> List[UserOut]:
    users = await User.all().only("username", "id_telegram")
    return [UserOut.from_orm(user) for user in users] if users else []


@router.get("/users/{id_telegram}")
async def get_user(id_telegram: str) -> UserOut:
    user = await User.get(id_telegram=id_telegram).only('file_path')
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    file_path = user.file_path
    return FileResponse(file_path)