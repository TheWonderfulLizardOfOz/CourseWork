from discord.ext import commands
import random
import sqlite3

class Class(commands.Cog):
    def __init__(self, bot = None):
        self.bot = bot
        self.classList = self.createClassList()

    def createClassList(self):
        self.openDB()
        self.cursor.execute("""SELECT className FROM class""")
        classes = self.cursor.fetchall()
        self.closeDB()
        classList = [className[0] for className in classes]
        return classList

    @commands.command()
    async def randomClass(self, ctx):
        await ctx.send(random.choice(self.classList))

    @commands.command()
    async def classDetails(self, ctx, arg):
        self.getClassDetails(arg)
        message = ""
        for key, value in self.classDetailsDict.items():
            message += "**`{}:`** {}\n".format(key, value)
        await ctx.send(message)

    def getClassDetails(self, arg):
        self.openDB()
        statement = """SELECT * FROM class WHERE class.className =  '""" + str(arg) + "'"
        self.cursor.execute(statement)
        classDetails = self.cursor.fetchall()[0]
        self.toolProficiencyType = None
        if classDetails[4] != None:
            statement = """SELECT toolType.toolType FROM toolType WHERE toolType.toolTypeID = """ + str(classDetails[4])
            self.cursor.execute(statement)
            self.toolProficiencyType = self.cursor.fetchall()[0]
        self.closeDB()
        print(classDetails)

        self.classID = classDetails[0]
        self.className = classDetails[1]
        self.hitDice = classDetails[2]
        self.noTools = classDetails[3]
        self.toolTypeID = classDetails[4]
        self.noSkills = classDetails[5]
        self.lightArmourProf = self.setValue(classDetails[6])
        self.mediumArmourProf = self.setValue(classDetails[7])
        self.heavyArmourProf = self.setValue(classDetails[8])
        self.shieldProf = self.setValue(classDetails[9])
        self.savingThrowOne = classDetails[10]
        self.savingThrowTwo = classDetails[11]
        self.weaponProf = self.setValue(classDetails[12])
        self.weaponRangeProf = self.setValue(classDetails[13])


        self.classDetailsDict = {"Class name": self.className, "Hit dice": "d" + str(self.hitDice),
                                 "Number of available tool proficiencies": self.noTools,
                                 "Type of tool proficiency": self.toolProficiencyType,
                                 "Number of available skills": self.noSkills,
                                 "Proficiency in Light Armour": self.lightArmourProf,
                                 "Proficiency in medium Armour": self.mediumArmourProf,
                                 "Proficiency in heavy Armour": self.heavyArmourProf,
                                 "Proficiency in shields": self.shieldProf,
                                 "Saving throws": [self.savingThrowOne, self.savingThrowTwo],
                                 "Weapon proficiencies": self.weaponProf,
                                 "Proficiency range": self.weaponRangeProf}

    def setValue(self, value):
        if value == 0:
            return False
        else:
            return True

    def openDB(self):
        self.db = sqlite3.connect("dndDB.db")
        self.cursor = self.db.cursor()

    def closeDB(self):
        self.db.commit()
        self.db.close()

def setup(bot):
    bot.add_cog(Class(bot))