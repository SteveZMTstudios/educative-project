from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...db import SessionLocal
from ... import models
from ... import schemas
from uuid import uuid4
import secrets
import hashlib
from datetime import datetime

try:
    from nacl.signing import SigningKey
except Exception:
    SigningKey = None


router = APIRouter(prefix="/auth", tags=["auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def backend_hash(client_sha256_hex: str, salt: str) -> str:
    # 接收前端 sha256 hex（字符串），后端将其与 salt 再 sha256
    combined = (client_sha256_hex + salt).encode('utf-8')
    return hashlib.sha256(combined).hexdigest()


@router.post("/register", response_model=schemas.UserOut)
def register(payload: schemas.RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == payload.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="username already exists")

    salt = secrets.token_hex(16)
    stored = backend_hash(payload.password, salt)

    user = models.User(
        username=payload.username,
        email=payload.email,
        password=stored,
        salt=salt,
        interest_tags="#newuser",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "interest_tags": user.interest_tags,
        "registration_time": user.registration_time,
        "last_login_time": user.last_login_time,
        "type": user.type,
        "class_code": None if user.class_ == 'none' else user.class_,
    }


@router.post("/login", response_model=schemas.Token)
def login(payload: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == payload.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="invalid credentials")

    # 验证前端发来的 sha256，再加 salt
    if backend_hash(payload.password, user.salt) != user.password:
        raise HTTPException(status_code=401, detail="invalid credentials")

    token = str(uuid4())
    user.token = token
    user.last_login_time = datetime.utcnow()

    # 生成 ed25519 密钥对（如果可用）
    if SigningKey is not None and (not user.private_key or not user.public_key):
        sk = SigningKey.generate()
        pk = sk.verify_key
        user.private_key = sk.encode().hex()
        user.public_key = pk.encode().hex()

    db.add(user)
    db.commit()
    return {"token": token}


@router.get("/me", response_model=schemas.MeWithKey)
def me(token: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.token == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="invalid token")
    # 仅返回 private_key 给已登录用户（此接口本身需要 token）
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "interest_tags": user.interest_tags,
        "registration_time": user.registration_time.isoformat() if user.registration_time else None,
        "last_login_time": user.last_login_time.isoformat() if user.last_login_time else None,
        "private_key": user.private_key,
        "type": user.type,
        "class_code": None if user.class_ == 'none' else user.class_,
    }



@router.post('/tags')
def update_tags(payload: schemas.UpdateInterestRequest, db: Session = Depends(get_db)):
    # payload: token and tags list
    token = payload.token
    tags = payload.tags
    if not token or not isinstance(tags, list):
        raise HTTPException(status_code=400, detail='token and tags list required')

    user = db.query(models.User).filter(models.User.token == token).first()
    if not user:
        raise HTTPException(status_code=401, detail='invalid token')

    user.interest_tags = ','.join(tags)
    if payload.user_type in ['teacher', 'student', 'user']:
        user.type = payload.user_type
    if payload.class_code:
        user.class_ = payload.class_code
    db.add(user)
    db.commit()
    return {"status": "ok", "interest_tags": user.interest_tags, "type": user.type, "class_code": None if user.class_ == 'none' else user.class_}
