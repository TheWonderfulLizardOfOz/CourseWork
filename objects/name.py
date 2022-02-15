from discord.ext import commands
import random

class Name(commands.Cog):
    def __init__(self, bot = None):
        self.bot = bot
        self.namesList = []
        file = open("names.txt", "r")
        for name in file:
            self.namesList.append(name.strip(",\n"))
        file.close()

    @commands.command()
    async def randomName(self, ctx):
        await ctx.send(random.choice(self.namesList))

    @commands.command()
    async def addName(self, ctx, arg):
        file = open("names.txt", "a")
        file.write(arg + ",\n")
        await ctx.send("Name added")

def setup(bot):
    bot.add_cog(Name(bot))