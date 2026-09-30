
from telethon import events
from bot.config import PREFIX, is_owner
from bot.state import AFK

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}afk(?: (.+))?$"))
    async def afk(e):
        if not is_owner(e.sender_id): return
        reason = e.pattern_match.group(1) or "AFK"
        AFK[e.sender_id] = reason
        await e.edit(f"💤 AFK enabled: {reason}")

    @client.on(events.NewMessage())
    async def watch(e):
        if e.sender_id in AFK and not e.raw_text.startswith(PREFIX):
            reason = AFK.pop(e.sender_id)
            await e.reply(f"👋 Welcome back! You were AFK: {reason}")
