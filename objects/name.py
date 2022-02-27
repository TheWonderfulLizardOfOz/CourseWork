from discord.ext import commands
import random

class Name(commands.Cog):
    def __init__(self, bot = None):
        self.bot = bot
        self.namesList = []
        file = open("names.txt", "r")
        #Iterates through every name in the file and adds them to the nameList attribute
        for name in file:
            self.namesList.append(name.strip(",\n"))
        file.close()

    #Selects a random name from the namesList attribute and sends it to the user
    @commands.command()
    async def randomName(self, ctx):
        await ctx.send(random.choice(self.namesList))

    @commands.command()
    async def addName(self, ctx, *args):
        #Validates the user input
        if len(args) == 0:
            valid = False
        else:
            #Iterates through every argument to check if they are valid if one argument is found to be invalid the loop breaks
            for arg in args:
                valid = self.validateNameInput(arg)
                if valid == False:
                    break
        if valid == False:
            #Sends message to user to tell them that their input was invalid
            await ctx.send("Invalid input, can't be empty, new lines and commas cannot be used.")
        else:
            #If user input is valid name is added to file
            name = ""
            for arg in args:
                #Adds arg and a whitespace to have a space between words
                name += arg + " "
            #Removes white space on last iteration
            name = name[0:-1]
            self.addNameToFile(name)
            #Sends message to user to tell them that the name was added to the file
            await ctx.send("Name added")

    #Method used to add name to file
    def addNameToFile(self, name):
        file = open("names.txt", "a")
        #Formats the name to have the first letter of every word be uppercase and everything else lowercase
        name = name.title()
        file.write(name + ",\n")
        file.close()
        self.namesList.append(name)

    #Method used to validate the user input
    def validateNameInput(self, userInput):
        if r"\n" in userInput or "," in userInput or userInput.isspace() == True or userInput == "":
            return False
        else:
            return True

def setup(bot):
    bot.add_cog(Name(bot))