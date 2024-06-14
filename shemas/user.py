from typing import Optional, List, Union, Dict, Any
from icecream import ic
from pydantic import BaseModel, EmailStr, Field
from pydantic.v1 import validator
from pydantic import BaseConfig


class UserOut(BaseModel):
    username: Optional[str] = None
    id_telegram: Optional[str] = None
    file_path: Optional[str] = None

    class Config(BaseConfig):
        orm_mode = True
        from_attributes = True


class UserFilePath(BaseModel):
    file_path: str
