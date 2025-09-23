from sqlalchemy import Column, Integer, String, Text, DateTime
from .db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True, index=True, nullable=False)
    email = Column(String(128), unique=True, index=True, nullable=True)
    password = Column(String(256), nullable=False)  # 存储后端加盐后的 sha256 hex
    salt = Column(String(64), nullable=False)
    token = Column(String(128), nullable=True)
    interest_tags = Column(String(256), nullable=False, default="#newuser")
    registration_time = Column(DateTime, default=datetime.utcnow)
    last_login_time = Column(DateTime, nullable=True)
    profile = Column(Text, nullable=True)
    public_key = Column(Text, nullable=True)
    private_key = Column(Text, nullable=True)
    # 新增：用户类型(user / teacher / student)
    type = Column(String(16), nullable=False, default="user")
    # 新增：所属班级（none 或班级代码）
    class_ = Column("class", String(64), nullable=False, default="none")
