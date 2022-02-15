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
        valid = self.validateNameInput(arg)
        if valid == False:
            await ctx.send("Invalid input, new lines and commas cannot be used.")
        else:
            file = open("names.txt", "a")
            arg = arg.title()
            file.write(arg + ",\n")
            file.close()
            self.namesList.append(arg)
            await ctx.send("Name added")

    def validateNameInput(self, userInput):
        if r"\n" in userInput or "," in userInput:
            return False
        else:
            return True

def setup(bot):
    bot.add_cog(Name(bot))