from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","ʜᴇʀᴏx 2.0 ᴍᴜsɪᴄ")
BOT_USERNAME = getenv("BOT_USERNAME", "tricky_1_musicbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "herox_xd")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Amtrickyabhi")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph//file/d85afcae9594b67582e1e.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/0712b7a27768966eea64c.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5124507794").split()))
