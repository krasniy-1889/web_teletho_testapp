from telethon import TelegramClient, events, sync
from config import config

api_id = config.API_ID
api_hash = config.API_HASH

client = TelegramClient("session_name", api_id, api_hash)
client.start()


@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("Hello test web app!")
