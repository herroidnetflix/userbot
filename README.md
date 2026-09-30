# BalaUserBot — Full Modular Starter

## Included modules
Core, account utilities, moderation, notes, filters, AFK, media saving,
utility commands, admin helpers, entertainment placeholders, search placeholder,
plugin loading and Docker deployment.

## Commands
`.ping` `.alive` `.help` `.id` `.info`
`.afk [reason]` `.save <name> <text>` `.get <name>` `.notes`
`.filter <word> <reply>` `.del` `.purge [count]`
`.kick` `.ban` `.unban` `.save` `.echo <text>` `.say <text>`
`.time` `.movie` `.cricket` `.song` `.search <query>`

## Setup
Copy `.env.example` to `.env`, fill `API_ID`, `API_HASH`, and either
`SESSION_STRING` for a user account or `BOT_TOKEN` for a bot account.

Never commit `.env` or a Telegram session to GitHub.

## Run
pip install -r requirements.txt
python -m bot.main

## Docker
docker compose up -d --build

Some integrations (search, movie, cricket, song) intentionally use safe
placeholders until their APIs are configured. Avoid spam, bulk messaging,
or other abusive automation and follow Telegram's rules.
