
from telethon import events
from bot.config import PREFIX, is_owner

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}lock (.+)$"))
    async def lock(e):
        if is_owner(e.sender_id):
            await e.edit("🔒 Lock configuration saved for: " + e.pattern_match.group(1))

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}unlock (.+)$"))
    async def unlock(e):
        if is_owner(e.sender_id):
            await e.edit("🔓 Unlock configuration saved for: " + e.pattern_match.group(1))
