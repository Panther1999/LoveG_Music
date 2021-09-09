import requests
from pyrogram import Client as Bot

from LoveG_Music.config import API_HASH
from LoveG_Music.config import API_ID
from LoveG_Music.config import BG_IMAGE
from LoveG_Music.config import BOT_TOKEN
from LoveG_Music.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="LoveG_Music.modules"),
)

bot.start()
run()
