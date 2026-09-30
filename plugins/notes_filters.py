
from telethon import events
from bot.config import PREFIX, is_owner
from bot.state import NOTES, FILTERS

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}save ([\w-]+) (.+)$"))
    async def save(e):
        if not is_owner(e.sender_id): return
        NOTES[e.pattern_match.group(1).lower()] = e.pattern_match.group(2)
        await e.edit("💾 Saved.")

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}get ([\w-]+)$"))
    async def get(e):
        await e.edit(NOTES.get(e.pattern_match.group(1).lower(), "❌ Note not found."))

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}notes$"))
    async def notes(e):
        await e.edit("📝 " + (", ".join(sorted(NOTES)) or "No notes."))

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}filter ([\w-]+) (.+)$"))
    async def add_filter(e):
        if not is_owner(e.sender_id): return
        FILTERS[e.pattern_match.group(1).lower()] = e.pattern_match.group(2)
        await e.edit("🔎 Filter saved.")

    @client.on(events.NewMessage())
    async def run_filters(e):
        if not e.raw_text or e.raw_text.startswith(PREFIX): return
        text = e.raw_text.lower()
        for key, response in FILTERS.items():
            if key in text:
                await e.reply(response)
                break
