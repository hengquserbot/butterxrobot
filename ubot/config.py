import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1054295664,
    1755047203,
    1898065191,
    2133148961,
    5876222922,
    1889573907,
    1966129176,
    5063062493,
    1810243126,
    1936017380,
    6002994221,
    2073506739,
    2033762302,
    793488327,
    5357942628,
    5013987239,
    876054262,
    1964437366,
    5703310502,
    5272203652,
]

<<<<<<< HEAD
KYNAN = list(map(int, os.getenv("ARTHUR", "").split()))
=======
KYNAN = list(map(int, os.getenv("ARTHUR", "1054295664 5272203652 5013987239 5357942628 1898065191").split()))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

<<<<<<< HEAD
API_ID = int(os.getenv("API_ID", ""))
=======
API_ID = int(os.getenv("API_ID", "22527580"))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

<<<<<<< HEAD
API_HASH = os.getenv("API_HASH", "")
=======
API_HASH = os.getenv("API_HASH", "2ca384a5fdf3c2ed1b7702869a2db439")
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

BOT_TOKEN = os.getenv("BOT_TOKEN", "6742667446:AAFhjpdI7m6Pk1MZz0fS6qP9LFb0idcTQkE")

SESSION = os.getenv("SESSION", "")

<<<<<<< HEAD
OWNER_ID = int(os.getenv("OWNER_ID", ""))
=======
OWNER_ID = int(os.getenv("OWNER_ID", "5272203652"))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

<<<<<<< HEAD
USER_ID = list(map(int, os.getenv("USER_ID", "").split()))
=======
USER_ID = list(map(int, os.getenv("USER_ID", "1054295664 5272203652 5013987239 1898065191 5357942628 816526222 6104161118").split()))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

<<<<<<< HEAD
LOG_UBOT = int(os.getenv("LOG_UBOT", ""))
=======
LOG_UBOT = int(os.getenv("LOG_UBOT", "-1002063271971"))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002063271971 -1001608847572 -1001538826310 -1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

RMBG_API = os.getenv("RMBG_API", "")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
<<<<<<< HEAD
    "",
=======
    "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",
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://chelluserbot:Chell1234@cluster0.0bpin1c.mongodb.net/chelluserbot?retryWrites=true&w=majority",
)
