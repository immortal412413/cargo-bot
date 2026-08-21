
import os
import discord
from discord.ext import commands

TOKEN = os.environ["TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL"])
ROLE_ID = int(os.environ["ROLE"])

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def test(ctx):
    embed = discord.Embed(
        title="🚢 Cargo Ship Spawned!",
        description="This is a test notification.",
        color=0x3498DB
    )

    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"<@&{ROLE_ID}>", embed=embed)
    await ctx.reply("✅ Test sent!")

bot.run(TOKEN)
