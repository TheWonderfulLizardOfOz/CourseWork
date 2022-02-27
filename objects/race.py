from discord.ext import commands
import random
import json

class Races(commands.Cog):
    def __init__(self, bot=None):
        self.bot = bot
        file = open("races.json")
        #json.load() converts into dictionary
        self.racesDict = json.load(file)
        file.close()
        #Creates a list of races using list comprehension by iterating through the keys in the dictionary
        self.raceList = [key for key in self.racesDict]

    @commands.command()
    async def randomRace(self, ctx):
        await ctx.send(random.choice(self.raceList))

    @commands.command()
    async def raceDetails(self, ctx, arg = None):
        value = None
        #if arg == None or value == None the the user input is not valid and will send an error message to the user
        if arg != None:
            arg = arg.title()
            value = self.racesDict.get(arg)
        if value != None:
            #Creates a message using the specific race dictionary
            message = self.createMessage(value)
            await ctx.send(message)
        else:
            listMessage = ""
            #Iterates through the list and adds items to the end of the message
            for item in self.raceList:
                listMessage += item + ", "
            #Removes las two characters which are ", "
            listMessage = listMessage[0:-2]
            #Error message that will be sent to the user
            await ctx.send("Race not stored\nCurrent available races are: {}".format(listMessage))

    def createMessage(self, dict):
        message = ""
        #Iterates through key value pairs in the dictionary
        for key, value in dict.items():
            valueOutput = ""
            #There are 2 possible data types for the values: int or list
            #If it is an int then a "+" will be placed in front
            if type(value) is int:
                valueOutput = "+" + str(value)
            #If it is a list then the items will be iterated through into an easier to read format for the user
            elif type(value) is list:
                for item in value:
                    valueOutput += item + ", "
                #Romoves last 2 characters ", "
                valueOutput = valueOutput[0:-2]
            message += "**`{}:`** {}\n".format(key.title(), valueOutput)
        return message

def setup(bot):
    bot.add_cog(Races(bot))