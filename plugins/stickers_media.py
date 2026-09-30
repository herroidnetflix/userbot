
from telethon import events
from bot.config import PREFIX, is_owner

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}save$"))
    async def save(e):
        r = await e.get_reply_message()
        if not r or not r.media:
            await e.edit("Reply to a media message.")
            return
        if not is_owner(e.sender_id): return
        await e.edit("📥 Downloading…")
        path = await client.download_media(r)
        await client.send_file("me", path, caption="Saved by BalaUserBot")
        await e.delete()
