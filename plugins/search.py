
from telethon import events
from bot.config import PREFIX

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}search (.+)$"))
    async def search(e):
        q = e.pattern_match.group(1)
        await e.edit(f"🔎 Search integration placeholder for: `{q}`")
