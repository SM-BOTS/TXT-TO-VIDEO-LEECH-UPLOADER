

from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/bot_subscription")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "7562079827").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "7562079827"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://gxmon239:f4l7bKrhka3Fh2cV@cluster0.qmblwql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")





