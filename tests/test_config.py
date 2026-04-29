import json
import time
from base64 import urlsafe_b64encode

from publicdotcom_cli.config import (
    ACCOUNT_ID_ENV_VAR,
    clear_default_account_id,
    get_default_account_id,
    set_default_account_id,
    token_expires_soon,
)


def _jwt_with_exp(expires_at: int) -> str:
    header = urlsafe_b64encode(json.dumps({"alg": "none"}).encode()).decode().rstrip("=")
    payload = urlsafe_b64encode(json.dumps({"exp": expires_at}).encode()).decode().rstrip("=")
    return f"{header}.{payload}."


def test_token_expires_soon_when_missing() -> None:
    assert token_expires_soon(None)


def test_token_expires_soon_uses_jwt_exp_with_skew() -> None:
    assert token_expires_soon(_jwt_with_exp(int(time.time()) + 30), skew_seconds=60)
    assert not token_expires_soon(_jwt_with_exp(int(time.time()) + 120), skew_seconds=60)


def test_token_expires_soon_ignores_unparseable_tokens() -> None:
    assert not token_expires_soon("not-a-jwt")
    assert not token_expires_soon("a.b.")


def test_default_account_id_round_trips_to_settings_file(tmp_path, monkeypatch) -> None:
    settings_path = tmp_path / "settings.json"
    monkeypatch.setattr("publicdotcom_cli.config.settings_file", lambda: settings_path)
    monkeypatch.delenv(ACCOUNT_ID_ENV_VAR, raising=False)

    assert get_default_account_id() is None
    assert set_default_account_id("account-123") == str(settings_path)
    assert get_default_account_id() == "account-123"

    clear_default_account_id()
    assert get_default_account_id() is None
    assert not settings_path.exists()


def test_default_account_id_env_var_takes_precedence(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("publicdotcom_cli.config.settings_file", lambda: tmp_path / "settings.json")
    monkeypatch.setenv(ACCOUNT_ID_ENV_VAR, "env-account")

    set_default_account_id("stored-account")

    assert get_default_account_id() == "env-account"
