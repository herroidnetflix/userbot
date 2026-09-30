
from telethon import events
from bot.config import PREFIX

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}movie$"))
    async def movie(e):
        await e.edit("🎬 Movie module ready. Connect TMDB/OMDb through environment variables.")

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}cricket$"))
    async def cricket(e):
        await e.edit("🏏 Cricket module ready. Connect a cricket API through environment variables.")

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}song$"))
    async def song(e):
        await e.edit("🎵 Song module ready for metadata/API integration.")
