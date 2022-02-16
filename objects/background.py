from discord.ext import commands
import sqlite3
import random

class Background(commands.Cog):
    #Default value of bot is None as when called by subclass that dosn't use the discord bot won't pass a value
    def __init__(self, bot = None):
        self.bot = bot
        self.backgroundID = -1
        self.background = ""
        self.personality = ""
        self.ideal = ""
        self.bond = ""
        self.flaw = ""
        self.noLanguages = -1
        self.personalityStatement = ""
        self.idealStatement = ""
        self.bondStatement = ""
        self.flawStatement = ""

    #Executes SQL statement to get a list of backgrounds
    def getBackgroundList(self):
        self.openDB()
        self.cursor.execute("""SELECT backgroundID, backgroundName, languagesNo FROM background""")
        backgroundList = self.cursor.fetchall()
        self.closeDB()
        return backgroundList

    #Executes SQL statement to get a list of features
    def getFeatureList(self, statement):
        self.openDB()
        self.cursor.execute(statement)
        featureList = self.cursor.fetchall()
        self.closeDB()
        return featureList

    #Sets the statements for fetching the required feature lists based off of the backgroundID
    def setStatements(self):
        self.personalityStatement = """SELECT personalityTrait.personalityTrait 
                           FROM PersonalityTrait WHERE personalityTrait.backgroundID = """ + str(self.backgroundID)
        self.idealStatement = """SELECT ideal.ideal FROM ideal WHERE ideal.backgroundID = """ + str(self.backgroundID)
        self.bondStatement = """SELECT bond.bond FROM bond WHERE bond.backgroundID = """ + str(self.backgroundID)
        self.flawStatement = """SELECT flaw.flaw FROM flaw WHERE flaw.backgroundID = """ + str(self.backgroundID)

    #openDB and closeDB are used to save time as they condese what would be 4 lines of code into 2 when called
    def openDB(self):
        self.db = sqlite3.connect("dndDB.db")
        self.cursor = self.db.cursor()

    def closeDB(self):
        self.db.commit()
        self.db.close()

class RandomBackground(Background):
    def __init__(self, bot):
        super().__init__(bot)
        self.message = ""

    @commands.command()
    async def randomBackground(self, ctx):
        backgroundList = self.getBackgroundList()
        self.setBackground(backgroundList)

        self.setStatements()

        personalityList = self.getFeatureList(self.personalityStatement)
        self.personality = self.setFeature(personalityList)

        idealList = self.getFeatureList(self.idealStatement)
        self.ideal = self.setFeature(idealList)

        bondList = self.getFeatureList(self.bondStatement)
        self.bond = self.setFeature(bondList)

        flawList = self.getFeatureList(self.flawStatement)
        self.flaw = self.setFeature(flawList)

        self.message = self.setMessage()

        await ctx.send(self.message)

    @commands.command()
    async def fullRandomBackground(self, ctx):
        pass

    def setStatementsFullRandom(self):
        self.personalityStatement = "SELECT personalityTrait.personalityTrait FROM PersonalityTrait"
        self.idealStatement = "SELECT ideal.ideal FROM ideal"
        self.bondStatement = "SELECT bond.bond FROM bond"
        self.flawStatement = "SELECT flaw.flaw FROM flaw"

    def setBackground(self, backgroundList):
        (self.backgroundID, self.background, self.languagesNo) = random.choice(backgroundList)

    #Selects a random choice from the list passed into the method
    def setFeature(self, featureList):
        feature = random.choice(featureList)[0]
        return feature

    #Method will return the message that will be output by the discord bot
    def setMessage(self):
        message = """**`Background:`** {}
**`Personality Trait:`** {}
**`Ideal:`** {}
**`Bond:`** {}
**`Flaw:`** {}""".format(self.background, self.personality, self.ideal, self.bond, self.flaw)
        return message

def setup(bot):
    bot.add_cog(RandomBackground(bot))