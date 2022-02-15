from discord.ext import commands
import random
import json

class Races(commands.Cog):
    def __init__(self, bot=None):
        self.bot = bot
        self.namesList = []
        file = open("races.json")
        self.racesDict = json.load(file)
        file.close()
        self.raceList = [value for value in self.racesDict]

    @commands.command()
    async def randomRace(self, ctx):
        await ctx.send(random.choice(self.raceList))

    @commands.command()
    async def raceDetails(self, ctx, arg):
        value = self.racesDict.get(arg)
        if value != None:
            message = self.createMessage(value)
            await ctx.send(message)
        else:
            await ctx.send("Race not stored")

    def createMessage(self, dict):
        message = ""
        for key, value in dict.items():
            message += "**`{}:`** {}\n".format(key, value)
        return message

def setup(bot):
    bot.add_cog(Races(bot))