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
    async def addName(self, ctx, arg = None):
        if arg == None:
            valid = False
        else:
            valid = self.validateNameInput(arg)
        if valid == False:
            await ctx.send("Invalid input, can't be empty, new lines and commas cannot be used.")
        else:
            self.addNameToFile(arg)
            await ctx.send("Name added")

    def addNameToFile(self, name):
        file = open("names.txt", "a")
        name = name.title()
        file.write(name + ",\n")
        file.close()
        self.namesList.append(name)

    def validateNameInput(self, userInput):
        if r"\n" in userInput or "," in userInput or userInput.isspace() == True:
            return False
        else:
            return True

def setup(bot):
    bot.add_cog(Name(bot))