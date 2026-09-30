
from telethon import events
from bot.config import PREFIX

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}info$"))
    async def info(e):
        u = await e.get_sender()
        name = " ".join(x for x in [u.first_name, u.last_name] if x)
        await e.edit(
            "👤 **User Info**\n"
            f"ID: `{u.id}`\n"
            f"Username: @{u.username}" if u.username else
            "👤 **User Info**\n"
            f"ID: `{u.id}`\n"
            "Username: —"
        )
