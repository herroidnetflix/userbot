
from telethon import events
from bot.config import PREFIX, is_owner

def setup(client):
    async def target(e):
        r = await e.get_reply_message()
        return r.sender_id if r else None

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}del$"))
    async def delete(e):
        if not is_owner(e.sender_id): return
        r = await e.get_reply_message()
        if r: await r.delete()
        await e.delete()

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}purge(?: (\d+))?$"))
    async def purge(e):
        if not is_owner(e.sender_id): return
        n = int(e.pattern_match.group(1) or 10)
        n = max(1, min(n, 100))
        msgs = [m async for m in client.iter_messages(e.chat_id, limit=n + 1)]
        await client.delete_messages(e.chat_id, [m.id for m in msgs])

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}kick$"))
    async def kick(e):
        if not is_owner(e.sender_id): return
        uid = await target(e)
        if uid:
            await client.kick_participant(e.chat_id, uid)

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}ban$"))
    async def ban(e):
        if not is_owner(e.sender_id): return
        uid = await target(e)
        if uid:
            await client.edit_permissions(e.chat_id, uid, view_messages=False)

    @client.on(events.NewMessage(pattern=rf"^{PREFIX}unban$"))
    async def unban(e):
        if not is_owner(e.sender_id): return
        uid = await target(e)
        if uid:
            await client.edit_permissions(e.chat_id, uid, view_messages=True)
