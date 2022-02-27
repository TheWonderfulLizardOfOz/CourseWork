from discord.ext import commands
import random
import sqlite3

class Class(commands.Cog):
    def __init__(self, bot = None):
        self.bot = bot
        self.classList = self.createClassList()

    #Creates a list of available classes in database
    def createClassList(self):
        self.openDB()
        self.cursor.execute("""SELECT className FROM class""")
        classes = self.cursor.fetchall()
        self.closeDB()
        #Uses list comprehension to create classList due to the format of the data from the database
        classList = [className[0] for className in classes]
        return classList

    @commands.command()
    async def randomClass(self, ctx):
        await ctx.send(random.choice(self.classList))

    @commands.command()
    async def classDetails(self, ctx, arg = None):
        #Checks if argument is a valid class
        if arg == None or arg.title() not in self.classList:
            listMessage = ""
            #Iterates through every item in the list and adds them to the message
            for item in self.classList:
                listMessage += item + ", "
            #Removes last 2 characters of the string which are ", "
            listMessage = listMessage[0:-2]
            message = "Invalid input available classes are: {}".format(listMessage)
        else:
            arg = arg.title()
            self.getClassDetails(arg)
            message = ""
            #Iterates through the key value pairs in classDetailsDict and adds them to the message
            for key, value in self.classDetailsDict.items():
                message += "**`{}:`** {}\n".format(key, value)
        #Outputs message to the user on discord
        await ctx.send(message)

    def getClassDetails(self, arg):
        #Gets all the fields of the class table containing the class requested by the user
        self.openDB()
        statement = """SELECT * FROM class WHERE class.className =  '""" + str(arg) + "'"
        self.cursor.execute(statement)
        classDetails = self.cursor.fetchall()[0]
        #Sets a default value for tool proficiency type
        self.toolProficiencyType = None
        #If the class has a tool proficiency it collects the type of proficiency from the database
        if classDetails[4] != None:
            statement = """SELECT toolType.toolType FROM toolType WHERE toolType.toolTypeID = """ + str(classDetails[4])
            self.cursor.execute(statement)
            #First [0] to get access to first tuple in list then second [0] to get access to first item in tuple which is the tool proficiency type
            self.toolProficiencyType = self.cursor.fetchall()[0][0]
        self.closeDB()

        #Assigns all the values in the fields to attributes
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
        self.weaponProf = classDetails[12]
        self.weaponRangeProf = classDetails[13]

        #Creates a dictionary to make the output easier to create
        self.classDetailsDict = {"Class name": self.className, "Hit dice": "d" + str(self.hitDice),
                                 "Number of available tool proficiencies": self.noTools,
                                 "Type of tool proficiency": self.toolProficiencyType,
                                 "Number of available skills": self.noSkills,
                                 "Proficiency in Light Armour": self.lightArmourProf,
                                 "Proficiency in medium Armour": self.mediumArmourProf,
                                 "Proficiency in heavy Armour": self.heavyArmourProf,
                                 "Proficiency in shields": self.shieldProf,
                                 "Saving throws": self.savingThrowOne + ", " + self.savingThrowTwo,
                                 "Weapon proficiencies": self.weaponProf,
                                 "Proficiency range": self.weaponRangeProf}

    #Turns binary 0 or 1 into boolean
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