# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file (optional for local dev)
load_dotenv()

# Get token from environment
TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # or hardcode it for testing

if not TOKEN:
    raise ValueError("No Discord bot token found in environment variables.")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # Required if your bot reads messages
intents.guilds = True
intents.members = True  # Required if you use member join events, etc.

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Ready event
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

# Sample command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot
bot.run(TOKEN)
