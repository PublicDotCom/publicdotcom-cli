from __future__ import annotations

import json
import os
import time
from base64 import urlsafe_b64decode
from binascii import Error as BinasciiError
from pathlib import Path
from typing import Any

import keyring
from keyring.errors import KeyringError
from platformdirs import user_config_dir

SERVICE_NAME = "publicdotcom-cli"
TOKEN_USERNAME = "access-token"
SECRET_USERNAME = "personal-secret"
TOKEN_ENV_VAR = "PUBLIC_ACCESS_TOKEN"
SECRET_ENV_VAR = "PUBLIC_PERSONAL_SECRET"
ACCOUNT_ID_ENV_VAR = "PUBLIC_ACCOUNT_ID"
BASE_URL_ENV_VAR = "PUBLIC_API_BASE_URL"
AUTO_REFRESH_ENV_VAR = "PUBLIC_AUTO_REFRESH"
DEFAULT_BASE_URL = "https://api.public.com"


def token_file() -> Path:
    return Path(user_config_dir("publicdotcom-cli", "publicdotcom")) / "token.json"


def settings_file() -> Path:
    return Path(user_config_dir("publicdotcom-cli", "publicdotcom")) / "settings.json"


def _read_settings() -> dict[str, Any]:
    path = settings_file()
    if not path.exists():
        return {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    return data if isinstance(data, dict) else {}


def _write_settings(settings: dict[str, Any]) -> str:
    path = settings_file()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
    path.chmod(0o600)
    return str(path)


def get_token() -> str | None:
    env_token = os.getenv(TOKEN_ENV_VAR)
    if env_token:
        return env_token

    try:
        token = keyring.get_password(SERVICE_NAME, TOKEN_USERNAME)
    except (KeyringError, RuntimeError, ImportError):
        token = None

    if token:
        return token

    path = token_file()
    if not path.exists():
        return None

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None

    token = data.get("accessToken")
    return token if isinstance(token, str) and token else None


def get_personal_secret() -> str | None:
    env_secret = os.getenv(SECRET_ENV_VAR)
    if env_secret:
        return env_secret

    try:
        secret = keyring.get_password(SERVICE_NAME, SECRET_USERNAME)
    except (KeyringError, RuntimeError, ImportError):
        secret = None

    if secret:
        return secret

    path = token_file().with_name("secret.json")
    if not path.exists():
        return None

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None

    secret = data.get("personalSecret")
    return secret if isinstance(secret, str) and secret else None


def get_default_account_id() -> str | None:
    env_account_id = os.getenv(ACCOUNT_ID_ENV_VAR)
    if env_account_id:
        return env_account_id

    account_id = _read_settings().get("defaultAccountId")
    return account_id if isinstance(account_id, str) and account_id else None


def set_token(token: str) -> str:
    try:
        keyring.set_password(SERVICE_NAME, TOKEN_USERNAME, token)
        return "keyring"
    except (KeyringError, RuntimeError, ImportError):
        path = token_file()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"accessToken": token}, indent=2), encoding="utf-8")
        path.chmod(0o600)
        return str(path)


def set_personal_secret(secret: str) -> str:
    try:
        keyring.set_password(SERVICE_NAME, SECRET_USERNAME, secret)
        return "keyring"
    except (KeyringError, RuntimeError, ImportError):
        path = token_file().with_name("secret.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"personalSecret": secret}, indent=2), encoding="utf-8")
        path.chmod(0o600)
        return str(path)


def set_default_account_id(account_id: str) -> str:
    settings = _read_settings()
    settings["defaultAccountId"] = account_id
    return _write_settings(settings)


def clear_token() -> None:
    try:
        keyring.delete_password(SERVICE_NAME, TOKEN_USERNAME)
    except (KeyringError, RuntimeError, ImportError, keyring.errors.PasswordDeleteError):
        pass

    path = token_file()
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def clear_personal_secret() -> None:
    try:
        keyring.delete_password(SERVICE_NAME, SECRET_USERNAME)
    except (KeyringError, RuntimeError, ImportError, keyring.errors.PasswordDeleteError):
        pass

    path = token_file().with_name("secret.json")
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def clear_default_account_id() -> None:
    settings = _read_settings()
    settings.pop("defaultAccountId", None)
    path = settings_file()
    if settings:
        _write_settings(settings)
        return

    try:
        path.unlink()
    except FileNotFoundError:
        pass


def mask_token(token: str | None) -> str:
    if not token:
        return "not set"
    if len(token) <= 12:
        return "*" * len(token)
    return f"{token[:6]}...{token[-6:]}"


def _decode_jwt_payload(token: str) -> dict[str, Any] | None:
    parts = token.split(".")
    if len(parts) < 2:
        return None

    payload = parts[1]
    payload += "=" * (-len(payload) % 4)
    try:
        decoded = urlsafe_b64decode(payload.encode("ascii"))
        data = json.loads(decoded.decode("utf-8"))
    except (BinasciiError, ValueError, UnicodeDecodeError):
        return None

    return data if isinstance(data, dict) else None


def token_expires_soon(token: str | None, *, skew_seconds: int = 60) -> bool:
    if not token:
        return True

    payload = _decode_jwt_payload(token)
    if not payload:
        return False

    expires_at = payload.get("exp")
    if not isinstance(expires_at, int | float):
        return False

    return expires_at <= time.time() + skew_seconds
