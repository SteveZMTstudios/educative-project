from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# 前端需先对密码进行 sha256，再发送到后端。后端会对该 sha256 值再加盐 sha256 存储
class RegisterRequest(BaseModel):
    username: str
    email: Optional[EmailStr]
    password: str  # 前端已 sha256 的 hex


class LoginRequest(BaseModel):
    username: str
    password: str  # 前端已 sha256 的 hex


class UserOut(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr]
    interest_tags: Optional[str]
    registration_time: Optional[datetime]
    last_login_time: Optional[datetime]
    type: Optional[str] = "user"
    class_code: Optional[str] = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    token: str


class MeWithKey(UserOut):
    private_key: Optional[str]


class UpdateInterestRequest(BaseModel):
    token: str
    tags: List[str]
    user_type: Optional[str] = None  # teacher / student / user
    class_code: Optional[str] = None


class TeacherRegisterRequest(BaseModel):
    token: str
    course_name: str
    course_code: Optional[str] = None
    teacher_name: Optional[str] = None
    course_description: Optional[str] = None
    course_link: Optional[str] = None
