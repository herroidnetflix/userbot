
import asyncio
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from .config import API_ID, API_HASH, SESSION_STRING, BOT_TOKEN, validate
from .loader import load_plugins

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
log = logging.getLogger("BalaUserBot")

async def main():
    validate()
    session = StringSession(SESSION_STRING) if SESSION_STRING else "bot_session"
    client = TelegramClient(session, API_ID, API_HASH)
    if BOT_TOKEN:
        await client.start(bot_token=BOT_TOKEN)
    else:
        await client.start()
    loaded = load_plugins(client)
    log.info("Loaded plugins: %s", ", ".join(loaded))
    me = await client.get_me()
    log.info("Logged in as %s", getattr(me, "username", None) or me.id)
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
