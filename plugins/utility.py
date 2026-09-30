
import time
from telethon import events
from bot.config import PREFIX, is_owner

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}echo (.+)$"))
    async def echo(e):
        if is_owner(e.sender_id):
            await e.edit(e.pattern_match.group(1))

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}say (.+)$"))
    async def say(e):
        if is_owner(e.sender_id):
            await e.reply(e.pattern_match.group(1))
            await e.delete()

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}time$"))
    async def tm(e):
        await e.edit("🕒 " + time.strftime("%Y-%m-%d %H:%M:%S"))
