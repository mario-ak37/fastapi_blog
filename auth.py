from datetime import UTC, datetime, timedelta

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash

from config import settings

password_hash = PasswordHash.recommended()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/token")


# Hash a plain-text password for storage.
def hash_password(password: str) -> str:
    return password_hash.hash(password)


# Verify a plain-text password against a stored hash.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


# Create a signed JWT access token with an expiration time.
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key.get_secret_value(), algorithm=settings.algorithm
    )
    return encoded_jwt


# Validate a JWT access token and return its user id subject.
def verify_access_token(token: str) -> str | None:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key.get_secret_value(),
            algorithms=[settings.algorithm],
            options={"require": ["exp", "sub"]},
        )
    except jwt.InvalidTokenError:
        return None
    else:
        return payload.get("sub")
