import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='!')

extensions = ["objects.owner", "objects.background", "objects.name", "objects.race", "objects.classes"]

@bot.event
async def on_ready():
    print("bot is ready for stuff")

if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)

bot.run(TOKEN)