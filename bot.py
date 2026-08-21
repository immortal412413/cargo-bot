
import os
import discord
from discord.ext import commands

TOKEN = os.environ["TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL"])
ROLE_ID = int(os.environ["ROLE"])

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx):
    channel = bot.get_channel(CHANNEL_ID)

    embed = discord.Embed(
        title="🚢 Cargo Ship Spawned!",
        description="Storage Hunters Cargo Ship is LIVE!",
        color=0x3498DB
    )

    embed.add_field(name="Status", value="🟢 ACTIVE")
    embed.add_field(name="Time Left", value="15 minutes")

    await channel.send(f"<@&{ROLE_ID}>", embed=embed)
    await ctx.send("✅ Test notification sent!")

bot.run(TOKEN)
