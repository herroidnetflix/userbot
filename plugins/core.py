
from telethon import events
from bot.config import PREFIX, is_owner

def setup(client):
    @client.on(events.NewMessage(pattern=rf"^{PREFIX}ping$"))
    async def ping(e):
        await e.edit("🏓 Pong!")

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}alive$"))
    async def alive(e):
        await e.edit("✅ BalaUserBot is alive!")

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}id$"))
    async def ids(e):
        reply = await e.get_reply_message()
        await e.edit(f"🆔 `{reply.sender_id if reply else e.sender_id}`")

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}help$"))
    async def help_(e):
        await e.edit(
            "🤖 **BalaUserBot**\n\n"
            f"`{PREFIX}ping` `{PREFIX}alive` `{PREFIX}id`\n"
            f"`{PREFIX}info` `{PREFIX}afk` `{PREFIX}notes`\n"
            f"`{PREFIX}purge` `{PREFIX}del` `{PREFIX}ban` `{PREFIX}kick`\n"
            f"`{PREFIX}save` `{PREFIX}get` `{PREFIX}filter`\n"
            f"`{PREFIX}movie` `{PREFIX}cricket`"
        )
