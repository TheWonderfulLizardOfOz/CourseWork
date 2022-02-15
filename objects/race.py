from discord.ext import commands
import random
import json

class Races(commands.Cog):
    def __init__(self, bot=None):
        self.bot = bot
        file = open("races.json")
        self.racesDict = json.load(file)
        file.close()
        self.raceList = [value for value in self.racesDict]

    @commands.command()
    async def randomRace(self, ctx):
        await ctx.send(random.choice(self.raceList))

    @commands.command()
    async def raceDetails(self, ctx, arg = None):
        value = None
        if arg != None:
            arg = arg.title()
            value = self.racesDict.get(arg)
        if value != None:
            message = self.createMessage(value)
            await ctx.send(message)
        else:
            listMessage = ""
            for item in self.raceList:
                listMessage += item + ", "
            listMessage = listMessage[0:-2]
            await ctx.send("Race not stored\nCurrent available races are: {}".format(listMessage))

    def createMessage(self, dict):
        message = ""
        for key, value in dict.items():
            valueOutput = ""
            if type(value) is int:
                valueOutput = "+" + str(value)
            elif type(value) is list:
                for item in value:
                    valueOutput += item + ", "
                valueOutput = valueOutput[0:-2]
            message += "**`{}:`** {}\n".format(key.title(), valueOutput)
        return message

def setup(bot):
    bot.add_cog(Races(bot))