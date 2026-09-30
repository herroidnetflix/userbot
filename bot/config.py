
import os

def _ints(value):
    return {int(x.strip()) for x in value.split(",") if x.strip().isdigit()}

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
PREFIX = os.getenv("PREFIX", ".")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
SUDO_USERS = _ints(os.getenv("SUDO_USERS", ""))

def is_owner(user_id):
    return user_id == OWNER_ID or user_id in SUDO_USERS

def validate():
    missing = []
    if not API_ID: missing.append("API_ID")
    if not API_HASH: missing.append("API_HASH")
    if not SESSION_STRING and not BOT_TOKEN:
        missing.append("SESSION_STRING or BOT_TOKEN")
    if missing:
        raise RuntimeError("Missing environment variables: " + ", ".join(missing))
