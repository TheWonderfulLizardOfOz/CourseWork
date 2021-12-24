from discord.ext import commands
import sqlite3
import random

class Background(commands.Cog):
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

    def getBackgroundList(self):
        self.openDB()
        self.cursor.execute("""SELECT * FROM background""")
        backgroundList = self.cursor.fetchall()
        self.closeDB()
        return backgroundList

    def getPersonalityList(self):
        self.openDB()
        self.cursor.execute(self.personalityStatement)
        personalityList = self.cursor.fetchall()
        self.closeDB()
        return personalityList

    def getIdealList(self):
        self.openDB()
        self.cursor.execute(self.idealStatement)
        idealList = self.cursor.fetchall()
        self.closeDB()
        return idealList

    def getBondList(self):
        self.openDB()
        self.cursor.execute(self.bondStatement)
        bondList = self.cursor.fetchall()
        self.closeDB()
        return bondList

    def getFlawList(self):
        self.openDB()
        self.cursor.execute(self.flawStatement)
        flawList = self.cursor.fetchall()
        self.closeDB()
        return flawList

    def setStatements(self):
        self.personalityStatement = """SELECT personalityTrait.personalityTrait 
                           FROM PersonalityTrait WHERE personalityTrait.backgroundID = """ + str(self.backgroundID)
        self.idealStatement = """SELECT ideal.ideal FROM ideal WHERE ideal.backgroundID = """ + str(self.backgroundID)
        self.bondStatement = """SELECT bond.bond FROM bond WHERE bond.backgroundID = """ + str(self.backgroundID)
        self.flawStatement = """SELECT flaw.flaw FROM flaw WHERE flaw.backgroundID = """ + str(self.backgroundID)

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

        personalityList = self.getPersonalityList()
        self.setPersonality(personalityList)

        idealList = self.getIdealList()
        self.setIdeal(idealList)

        bondList = self.getBondList()
        self.setBond(bondList)

        flawList = self.getFlawList()
        self.setFlaw(flawList)

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

    def setPersonality(self, personalityList):
        self.personality = random.choice(personalityList)[0]

    def setIdeal(self, idealList):
        self.ideal = random.choice(idealList)[0]

    def setBond(self, bondList):
        self.bond = random.choice(bondList)[0]

    def setFlaw(self, flawList):
        self.flaw = random.choice(flawList)[0]

    def setMessage(self):
        message = """**`Background:`** {}
**`Personality Trait:`** {}
**`Ideal:`** {}
**`Bond:`** {}
**`Flaw:`** {}""".format(self.background, self.personality, self.ideal, self.bond, self.flaw)
        return message

def setup(bot):
    bot.add_cog(RandomBackground(bot))