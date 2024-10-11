import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1435108695,
]

<<<<<<< HEAD
HENGQ = list(map(int, os.getenv("ARTHUR", "").split()))
=======
HENKQ = list(map(int, os.getenv("ARTHUR", "1435108695").split()))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

<<<<<<< HEAD
API_ID = int(os.getenv("API_ID", ""))
=======
API_ID = int(os.getenv("API_ID", "17855094"))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

<<<<<<< HEAD
API_HASH = os.getenv("API_HASH", "")
=======
API_HASH = os.getenv("API_HASH", "004a12ddadfd7e96afa84af7f37e4fe6")
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

BOT_TOKEN = os.getenv("BOT_TOKEN", "7408701168:AAHcOTjV2ob4AvqWW5VNZHa72N6oHIbZEPk")

SESSION = os.getenv("SESSION", "")

<<<<<<< HEAD
OWNER_ID = int(os.getenv("OWNER_ID", ""))
=======
OWNER_ID = int(os.getenv("OWNER_ID", "1435108695"))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

<<<<<<< HEAD
USER_ID = list(map(int, os.getenv("USER_ID", "").split()))
=======
USER_ID = list(map(int, os.getenv("USER_ID", "1435108695").split()))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

<<<<<<< HEAD
LOG_UBOT = int(os.getenv("LOG_UBOT", ""))
=======
LOG_UBOT = int(os.getenv("LOG_UBOT", "--1002369567634"))
>>>>>>> dd496e293f887df8d2dbb65d6bec4d4f91f6dee3

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002226843410 -1002369567634").split()))

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
