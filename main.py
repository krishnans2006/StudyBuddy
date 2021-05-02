import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix=["s!"], description="StudyBuddy!")

cogs = ["cogs.setup", "cogs.current", "cogs.info"]
for cog in cogs:
    client.load_extension(cog)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Good Grades!"))
    print("Bot is ready!")

client.run(os.getenv("TOKEN"))