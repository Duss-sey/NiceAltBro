import discord
from discord.ext import commands
from aiohttp import web
import asyncio
import logging
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # or a direct string like "MTA..."
bot.run(TOKEN)


TOKEN = "MTM2OTQ5MDQ3MjIyMTAyMDMwMA.GnhXkG.6-385adQrXlIhkAAkBQQtv2seDaPtIGUvjEqM0"
GUILD_ID = 1110839856902459392  # e.g. 123456789012345678
VERIFIED_ROLE_NAME = "Verified"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Set up aiohttp web server
app = web.Application()
routes = web.RouteTableDef()

@routes.post("/verify")
async def handle_verification(request):
    try:
        data = await request.json()
        user_id = int(data["user_id"])
        username = data["username"]
        ip = data["ip"]

        guild = bot.get_guild(GUILD_ID)
        member = guild.get_member(user_id)

        if member:
            role = discord.utils.get(guild.roles, name=VERIFIED_ROLE_NAME)
            if role:
                await member.add_roles(role)
                await member.send("✅ You’ve been verified successfully!")
            else:
                print("❌ Verified role not found.")
        else:
            print(f"⚠️ Member not found in guild: {user_id} ({username})")
    except Exception as e:
        logging.exception("Failed to process verification webhook")

    return web.Response(text="OK")

app.add_routes(routes)

async def start_webserver():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)  # Port must match site config
    await site.start()
    print("🚀 Webhook server running on port 8080")

@bot.event
async def on_ready():
    print(f"Bot ready: {bot.user}")
    await start_webserver()

bot.run(TOKEN)
