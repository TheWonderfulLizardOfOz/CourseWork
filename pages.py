import tkinter as tk
import random
from objects.background import Background
from objects.name import Name
from objects.classes import Class
from objects.race import Races

#Class which allows universal methods for all the pages
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    #Used to lift a page to front making it visible to user
    def show(self):
        self.lift()

class CreateCharacterPage(Page, Background, Name, Class, Races):
    def __init__(self, *args, **kwargs):
        #Calls super class constructors
        Page.__init__(self, *args, **kwargs)
        Background.__init__(self)
        Name.__init__(self)
        Class.__init__(self)
        Races.__init__(self)

        self.openDB()
        self.closeDB()

        #Sets a default value for characterID to track if a character has been created
        self.characterID = None

        tempDefault = tk.StringVar(self)

        #Sets lists for option menus
        self.backgroundOptionList = [background[1] for background in self.getBackgroundList()]
        self.personalityOptionList = ["Select a background first"]
        self.idealOptionList = ["Select a background first"]
        self.bondOptionList = ["Select a background first"]
        self.flawOptionList = ["Select a background first"]
        self.setCharacterList()

        #Sets default values for option menus
        self.personality = tk.StringVar(self)
        self.ideal = tk.StringVar(self)
        self.bond = tk.StringVar(self)
        self.flaw = tk.StringVar(self)
        self.classChoice = tk.StringVar(self)
        self.classChoice.set("Select an option")
        self.race = tk.StringVar(self)
        self.race.set("Select an option")
        self.character = tk.StringVar(self)
        self.character.set("Load")
        self.deleteText = tk.StringVar(self)
        self.deleteText.set("Delete")
        #Places all the background feature option menu widgets
        #In its own method due to multiple occasions where these widgets have to be destroyed and recreated
        #So placing in its own method saves time and space
        self.placeBackgroundFeatureWidgets()

        self.background = tk.StringVar(self)
        self.background.set("Select an option")
        self.prevBackground = self.background.get()
        self.backgroundOption = tk.OptionMenu(self, self.background, *self.backgroundOptionList, command = self.backgroundUpdated)
        self.backgroundOption.place(relheight = 0.06, relwidth = "0.25", relx = "0.17", rely = "0.24")

        backgroundLabel = tk.Label(self, relief = "groove", text = "Background")
        backgroundLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely = "0.24")

        personalityLabel = tk.Label(self, relief = "groove", text = "Personality")
        personalityLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely = "0.3")

        idealLabel = tk.Label(self, relief = "groove", text = "Ideal")
        idealLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely="0.36")

        bondLabel = tk.Label(self, relief = "groove", text = "Bond")
        bondLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely = "0.42")

        flawLabel = tk.Label(self, relief = "groove", text = "Flaw")
        flawLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely = "0.48")

        randomBackgroundButton = tk.Button(self, text="Rand", command=lambda: self.randomOption(self.backgroundOptionList, self.background))
        randomBackgroundButton.place(relheight="0.06", relwidth="0.05", relx="0.42", rely="0.24")

        randomPersonalityButton = tk.Button(self, text = "Rand", command=lambda: self.randomOption(self.personalityOptionList, self.personality))
        randomPersonalityButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.42", rely = "0.3")

        randomIdealButton = tk.Button(self, text = "Rand", command=lambda: self.randomOption(self.idealOptionList, self.ideal))
        randomIdealButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.42", rely = "0.36")

        randomBondButton = tk.Button(self, text = "Rand", command=lambda: self.randomOption(self.bondOptionList, self.bond))
        randomBondButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.42", rely = "0.42")

        randomFlawButton = tk.Button(self, text = "Rand", command=lambda: self.randomOption(self.flawOptionList, self.flaw))
        randomFlawButton.place(relheight = "0.06", relwidth = 0.05, relx = "0.42", rely = "0.48")

        imageLabel = tk.Label(self, relief = "sunken", text = "Image")
        imageLabel.place(relheight = "0.45", relwidth = "0.45", relx = "0.53", rely = "0.03")

        uploadImageButton = tk.Button(self, text = "Upload Image")
        uploadImageButton.place(relheight = "0.06", relwidth = "0.225", relx = "0.53", rely = "0.48")

        randomImageButton = tk.Button(self, text = "Random Image")
        randomImageButton.place(relheight = "0.06", relwidth = "0.225", relx = "0.755", rely = "0.48")

        saveCharacterButton = tk.Button(self, text = "Save", command = self.saveCharacter)
        saveCharacterButton.place(relheight = 0.045, relwidth = "0.08", relx = "0.31", rely = "0.03")

        newCharacterButton = tk.Button(self, text = "New", command = self.newCharacter)
        newCharacterButton.place(relheight = 0.045, relwidth = "0.08", relx = "0.31", rely = "0.075")

        self.loadCharacterOptions = tk.OptionMenu(self, self.character, *self.characterList, command = self.loadCharacter)
        self.loadCharacterOptions.place(relheight = 0.045, relwidth = 0.08, relx = 0.39, rely = 0.03)

        self.deleteOptions = tk. OptionMenu(self, self.deleteText, *self.characterList, command = self.deleteCharacter)
        self.deleteOptions.place(relheight = 0.045, relwidth = 0.08, relx = 0.39, rely = 0.075)

        nameLabel = tk.Label(self, relief = "groove", text = "Name")
        nameLabel.place(relheight = "0.06", relwidth = "0.06", relx = "0.02", rely = "0.03")

        raceLabel = tk.Label(self, relief = "groove", text = "Race")
        raceLabel.place(relheight = "0.06", relwidth = "0.06", relx = "0.02", rely = "0.09")

        classLabel = tk.Label(self, relief = "groove", text = "Class")
        classLabel.place(relheight = "0.06", relwidth = "0.06", relx = "0.02", rely = "0.15")

        self.nameEntry = tk.Entry(self)
        self.nameEntry.place(relheight = "0.06", relwidth = "0.1", relx = "0.08", rely = "0.03")

        addName = tk.Button(self, text = "add", command = self.addName)
        addName.place(relheight = "0.06", relwidth = "0.05", relx = "0.18", rely = "0.03")

        randomNameButton = tk.Button(self, text="Rand", command=self.randomName)
        randomNameButton.place(relheight="0.06", relwidth="0.05", relx="0.23", rely="0.03")

        raceOption = tk.OptionMenu(self, self.race, *self.raceList)
        raceOption.place(relheight = "0.06", relwidth = "0.15", relx = "0.08", rely = "0.09")

        classOption = tk.OptionMenu(self, self.classChoice, *self.classList)
        classOption.place(relheight = "0.06", relwidth = "0.15", relx = "0.08", rely = "0.15")

        randomRaceButton = tk.Button(self, text = "Rand", command = lambda: self.randomOption(self.raceList, self.race))
        randomRaceButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.09")

        randomClassButton = tk.Button(self, text = "Rand", command = lambda: self.randomOption(self.classList, self.classChoice))
        randomClassButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.15")

        strengthLabel = tk.Label(self, relief = "groove", text = "Strength")
        strengthLabel.place(relheight = "0.06", relwidth = "0.15", relx= "0.02", rely="0.57")

        charismaLabel = tk.Label(self, relief = "groove", text = "Charisma")
        charismaLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely = "0.63")

        wisdomLabel = tk.Label(self, relief = "groove", text = "Wisdom")
        wisdomLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely = "0.69")

        intelligenceLabel = tk.Label(self, relief = "groove", text = "Intelligence")
        intelligenceLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely=0.75)

        dexterityLabel = tk.Label(self, relief = "groove", text = "Dexterity")
        dexterityLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely = "0.81")

        constitutionLabel = tk.Label(self, relief = "groove", text = "Constitution")
        constitutionLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.02", rely = "0.87")

        strengthEntry = tk.Entry(self)
        strengthEntry.place(relheight = "0.06", relwidth = "0.06", relx = "0.17", rely = "0.57")

        charismaEntry = tk.Entry(self)
        charismaEntry.place(relheight = "0.06", relwidth = "0.06", relx = "0.17", rely = "0.63")

        wisdomEntry = tk.Entry(self)
        wisdomEntry.place(relheight = "0.06", relwidth = "0.06", relx = "0.17", rely = "0.69")

        intelligenceEntry = tk.Entry(self)
        intelligenceEntry.place(relheight = "0.06", relwidth = "0.06", relx = "0.17", rely = "0.75")

        dexterityEntry = tk.Entry(self)
        dexterityEntry.place(relheight = "0.06", relwidth = "0.06", relx = "0.17", rely = "0.81")

        constitutionEntry = tk.Entry(self)
        constitutionEntry.place(relheight = "0.06", relwidth = "0.06", relx = "0.17", rely = "0.87")

        randomStrengthButton = tk.Button(self, text = "Rand")
        randomStrengthButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.57")

        randomCharismaButton = tk.Button(self, text = "Rand")
        randomCharismaButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.63")

        randomWisdomButton = tk.Button(self, text = "Rand")
        randomWisdomButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.69")

        randomIntelligenceButton = tk.Button(self, text = "Rand")
        randomIntelligenceButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.75")

        randomDexterityButton = tk.Button(self, text = "Rand")
        randomDexterityButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.81")

        randomConstitutionButton = tk.Button(self, text = "Rand")
        randomConstitutionButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.87")

        languagesLabel = tk.Label(self, relief = "groove", text = "Languages")
        languagesLabel.place(relheight = "0.06", relwidth = "0.1", relx = "0.32", rely = "0.60")

        self.languageOptionList = []
        languageOptionOne = tk.OptionMenu(self, tempDefault, None, self.languageOptionList)
        languageOptionOne.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.66")

        languageOptionTwo = tk.OptionMenu(self, tempDefault, None, self.languageOptionList)
        languageOptionTwo.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.72")

        languageOptionThree = tk.OptionMenu(self, tempDefault, None, self.languageOptionList)
        languageOptionThree.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.78")

        languageOptionFour = tk.OptionMenu(self, tempDefault, None, self.languageOptionList)
        languageOptionFour.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.84")

        randomLanguageButton = tk.Button(self, text="Rand")
        randomLanguageButton.place(relheight="0.06", relwidth=0.05, relx="0.42", rely="0.6")

        skillLabel = tk.Label(self, relief = "groove", text = "Skills")
        skillLabel.place(relheight = "0.06", relwidth = "0.16", relx = "0.53", rely = "0.57")

        self.skillOptionList = []
        skillOptionOne = tk.OptionMenu(self, tempDefault, None, self.skillOptionList)
        skillOptionOne.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.63")

        skillOptionTwo = tk.OptionMenu(self, tempDefault, None, self.skillOptionList)
        skillOptionTwo.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.69")

        skillOptionThree = tk.OptionMenu(self, tempDefault, None, self.skillOptionList)
        skillOptionThree.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.75")

        skillOptionFour = tk.OptionMenu(self, tempDefault, None, self.skillOptionList)
        skillOptionFour.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.81")

        skillOptionFive = tk.OptionMenu(self, tempDefault, None, self.skillOptionList)
        skillOptionFive.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.87")

        randomSkillButton = tk.Button(self, text="Rand")
        randomSkillButton.place(relheight="0.06", relwidth=0.05, relx="0.69", rely="0.57")

        toolLabel = tk.Label(self, relief = "groove", text = "Tools")
        toolLabel.place(relheight = "0.06", relwidth = "0.16", relx = "0.77", rely = "0.57")

        self.toolOptionList = []
        toolOptionOne = tk.OptionMenu(self, tempDefault, None, self.toolOptionList)
        toolOptionOne.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.63")

        toolOptionTwo = tk.OptionMenu(self, tempDefault, None, self.toolOptionList)
        toolOptionTwo.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.69")

        toolOptionThree = tk.OptionMenu(self, tempDefault, None, self.toolOptionList)
        toolOptionThree.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.75")

        toolOptionFour = tk.OptionMenu(self, tempDefault, None, self.toolOptionList)
        toolOptionFour.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.81")

        toolOptionFive = tk.OptionMenu(self, tempDefault, None, self.toolOptionList)
        toolOptionFive.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.87")

        randomToolButton = tk.Button(self, text="Rand")
        randomToolButton.place(relheight="0.06", relwidth=0.05, relx="0.93", rely="0.57")

        self.messageLabel = tk.Label(self, relief='sunken', text='Messages')
        self.messageLabel.place(relheight='0.09', relwidth='0.16', relx='0.31', rely='0.12')

    #Places all the background feature option menu widgets
    def placeBackgroundFeatureWidgets(self):
        self.personality.set("Select an option")
        self.personalityOption = tk.OptionMenu(self, self.personality, None, *self.personalityOptionList)
        self.personalityOption.place(relheight="0.06", relwidth="0.25", relx="0.17", rely="0.3")

        self.ideal.set("Select an option")
        self.idealOption = tk.OptionMenu(self, self.ideal, None, *self.idealOptionList)
        self.idealOption.place(relheight=0.06, relwidth="0.25", relx="0.17", rely="0.36")

        self.bond.set("Select an option")
        self.bondOption = tk.OptionMenu(self, self.bond, None, *self.bondOptionList)
        self.bondOption.place(relheight="0.06", relwidth="0.25", relx="0.17", rely="0.42")

        self.flaw.set("Select an option")
        self.flawOption = tk.OptionMenu(self, self.flaw, None, *self.flawOptionList)
        self.flawOption.place(relheight="0.06", relwidth="0.25", relx="0.17", rely="0.48")

    def setLists(self):
        self.backgroundOptionList = [background[1] for background in self.getBackgroundList()]
        self.personalityOptionList = [feature[0] for feature in self.getFeatureList(self.personalityStatement)]
        self.idealOptionList = [feature[0] for feature in self.getFeatureList(self.idealStatement)]
        self.bondOptionList = [feature[0] for feature in self.getFeatureList(self.bondStatement)]
        self.flawOptionList = [feature[0] for feature in self.getFeatureList(self.flawStatement)]

    #Runs when an option is selected in background option menu
    #Method used to reset values in other option menus related to background
    #As each background has unique background features
    def backgroundUpdated(self, *args):
        #Checks if background is same as previous, if same nothing happens
        self.newBackground = self.background.get()
        if self.newBackground == self.prevBackground:
            return
        else:
            self.prevBackground = self.newBackground

        self.openDB()
        #args[0] is the background name
        self.cursor.execute("""SELECT backgroundID FROM background WHERE backgroundName = ?""", [args[0]])
        self.backgroundID = self.cursor.fetchall()
        if len(self.backgroundID) != 0:
            self.backgroundID = self.backgroundID[0][0]
        else:
            self.backgroundID = -1
        self.closeDB()

        self.setStatements()
        self.setLists()

        self.personalityOption.destroy()
        self.idealOption.destroy()
        self.bondOption.destroy()
        self.flawOption.destroy()

        self.placeBackgroundFeatureWidgets()

    #Will set the value in the attribute passed to a randomly selected option in the list passed
    def randomOption(self, optionList, featureAttribute):
        featureAttribute.set(random.choice(optionList))
        #Checks if background was changed, if the background was changed then the feature option menus will be reset
        if featureAttribute.get() in self.backgroundOptionList:
            self.backgroundUpdated(featureAttribute.get())

    def randomName(self):
        nameSelection = random.choice(self.namesList)
        self.nameEntry.delete(0, tk.END)
        self.nameEntry.insert(0, nameSelection)

    def addName(self):
        name = self.nameEntry.get()
        if name != None:
            valid = self.validateNameInput(name)
        else:
            valid = False
        if valid == True:
            self.addNameToFile(name)
            # Updates messageLabel attribute to Filet the user know that a name was successfully added
            self.messageLabel["text"] = "Name added to file"
        elif valid == False:
            self.messageLabel["text"] = "Invalid Name"

    def saveCharacter(self):
        #Checks if name is valid before adding character to database
        if self.validateNameInput(self.nameEntry.get()) == False:
            #Lets the user know why there was an error
            self.messageLabel["text"] = "Invalid name"
            return

        #characterID does not need to be set as it is set automatically when adding a new record to  a database
        characterName = self.nameEntry.get()
        #race doesn't need to be set as it can be fetched using self.race.get()
        classID = self.getID("class", "classID", self.classChoice.get(), "className")
        #backgroundID does not need to be set as it is set everytime background is updated so there is already an attribute called self.backgroundID
        bondID = self.getID("bond", "bondID", self.bond.get(), "bond")
        flawID = self.getID("flaw", "flawID", self.flaw.get(), "flaw")
        idealID = self.getID("ideal", "idealID", self.ideal.get(), "ideal")
        personalityID = self.getID("personalityTrait", "personalityID", self.personality.get(), "personalityTrait")

        self.openDB()
        if self.characterID == None:
            #Insets entered details into database
            self.cursor.execute("""INSERT INTO characters(characterName, race,
            classID, backgroundID, bondID, flawID, idealID, personalityTraitID) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
                           (characterName, self.race.get(), classID, self.backgroundID,
                            bondID, flawID, idealID, personalityID))
            self.closeDB()
        else:
            sql = """UPDATE characters SET characterName = ?, race = ?, classID = ?, backgroundID = ?, bondID = ?, 
            flawID = ?, idealID = ?, personalityTraitID = ? WHERE characterID = ?"""
            values = (characterName, self.race.get(), classID, self.backgroundID,
                            bondID, flawID, idealID, personalityID, self.characterID)
            self.cursor.execute(sql, values)
            #Resets characterID as there is there is now no current character being edited
            self.characterID = None
            self.closeDB()

        #Resets the delete and load option menus so that relevant lists of characters can appear
        self.placeLoadAndDelete()
        #Resets the input widgets so that they are all cleared
        self.resetWidgets()
        self.prevBackground = None

        #Lets the user know that the character was successfully added
        self.messageLabel["text"] = "Character saved :)"

    #Gets the ID of the record where the value passed is stored
    #Used to construct SQL statements by saving time and can be reused multiple times when fetching IDs
    def getID(self, table, idField, value, valueField):
        statement = "SELECT " + table + "." + idField + " FROM " + table + " WHERE " + table + "." + valueField + " = '" + value + "'"
        self.openDB()
        self.cursor.execute(statement)
        results = self.cursor.fetchall()
        self.closeDB()

        #If the result is empty (no record containing value) than None is returned
        if len(results) == 0:
            return None

        return results[0][0]

    #resets entry and option menu widgets
    def resetWidgets(self):
        self.backgroundID = -1
        self.setStatements()
        self.setLists()
        self.placeBackgroundFeatureWidgets()
        self.nameEntry.delete(0, tk.END)
        self.race.set("Select an option")
        self.classChoice.set("Select an option")
        self.background.set("Select an option")

    def setCharacterList(self, *args):
        self.openDB()
        self.cursor.execute("SELECT characterID, characterName FROM characters")
        self.characterList = self.cursor.fetchall()
        self.closeDB()

    def loadCharacter(self, selection):
        #Resets widgets so that changes the user did before pressing load disappear
        self.resetWidgets()

        #Makes it so that the load button only says "Load" for ease of use for the user
        self.character.set("Load")
        #Sets a characterID so that it is used again when saving a character
        self.characterID = selection[0]
        self.openDB()
        self.cursor.execute("SELECT * FROM characters WHERE characterID = ?", [self.characterID])
        #Characer details will be a tuple storing the fetched information from the database
        #The tuple stores information from each field:
        #(characterID, characterName, classID, bondID, flawID, idealID, personalityTraitID, classSKillOneID, classSkillTwoID, classSkillThreeID, toolOneID, toolTwoID, toolThreeID, toolFourID, languageOneID, languageTwoID, languageThreeID, race)
        characterDetails = self.cursor.fetchall()[0]

        #Resets name entry and then inserts the name from the database which is in characterDetails[1]
        self.nameEntry.delete(0, tk.END)
        self.nameEntry.insert(0, characterDetails[1])

        #Checks if the record is not null before updating classChoice
        if characterDetails[2] != None:
            self.cursor.execute("SELECT className FROM class WHERE classID = ?", [characterDetails[2]])
            self.classChoice.set(self.cursor.fetchall()[0][0])

        #Checks if there is a background, before updating backgrounds
        if characterDetails[3] == -1 or characterDetails[3] == None:
            self.background.set("Select an option")
            self.closeDB()
            self.backgroundID = -1
            self.prevBackground = None
            self.setStatements()
            self.setLists()
            self.personalityOption.destroy()
            self.idealOption.destroy()
            self.bondOption.destroy()
            self.flawOption.destroy()
            self.placeBackgroundFeatureWidgets()
            self.openDB()

        #Checks if there is a background
        else:
            self.cursor.execute("SELECT backgroundName FROM background WHERE backgroundID = ?", [characterDetails[3]])
            self.background.set(self.cursor.fetchall()[0][0])
            self.closeDB()
            self.backgroundUpdated(self.background.get())
            self.backgroundID = characterDetails[3]
            self.openDB()

            #Background features in nested if statements so that they aren't run if there is no background as it would save time in that case
            if characterDetails[4] != None:
                self.cursor.execute("SELECT bond FROM bond WHERE bondID = ?", [characterDetails[4]])
                self.bond.set(self.cursor.fetchall()[0][0])

            if characterDetails[5] != None:
                self.cursor.execute("SELECT flaw FROM flaw WHERE flawID = ?", [characterDetails[5]])
                self.flaw.set(self.cursor.fetchall()[0][0])

            if characterDetails[6] != None:
                self.cursor.execute("SELECT ideal FROM ideal WHERE idealID = ?", [characterDetails[6]])
                self.ideal.set(self.cursor.fetchall()[0][0])

            if characterDetails[7] != None:
                self.cursor.execute("SELECT personalityTrait FROM personalityTrait WHERE personalityID = ?", [characterDetails[7]])
                self.personality.set(self.cursor.fetchall()[0][0])

        if characterDetails[18] != None:
            self.race.set(characterDetails[18])
        else:
            self.race.set("Select an option")
        self.closeDB()

    #Called when the new button is pressed, used to reset everything to what the GUI would look like when initially opened
    def newCharacter(self):
        self.resetWidgets()
        self.prevBackground = None
        self.characterID = None

    def deleteCharacter(self, *args):
        #Deletes record from database with the characterID of the selected option
        self.openDB()
        self.cursor.execute("DELETE FROM characters WHERE characterID = ?", (args[0][0],))
        self.closeDB()

        #Checks id the last loaded character is the same as the one being deleted, if they are it resets the input widgets
        if args[0][0] == self.characterID:
            self.characterID = None
            self.newCharacter()

        #Calls a method to reset the load and delete option menus to avoid the user trying to load or delete a character that has already been deleted
        self.placeLoadAndDelete()
        self.messageLabel["text"] ="Character deleted :("

    #Method used to reset the load and delete option menus when the characterList attribute needs to be updated due to a new character being added or another being deleted
    def placeLoadAndDelete(self):
        self.setCharacterList()

        #Sets the text in the option menus
        self.character.set("Load")
        self.deleteText.set("Delete")

        #Destroys them as when placing another one they will be placed on top so it avoids the widget being duplicated
        self.loadCharacterOptions.destroy()
        self.deleteOptions.destroy()

        #Places the widgets
        self.loadCharacterOptions = tk.OptionMenu(self, self.character, *self.characterList, command = self.loadCharacter)
        self.loadCharacterOptions.place(relheight=0.045, relwidth=0.08, relx=0.39, rely=0.03)

        self.deleteOptions = tk.OptionMenu(self, self.deleteText, *self.characterList, command = self.deleteCharacter)
        self.deleteOptions.place(relheight=0.045, relwidth=0.08, relx=0.39, rely=0.075)

class BattlePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

class DicePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

class CharacterSheetPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

class ItemsAndSpellsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

class AddItemsAndSpellsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

class SettingsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.root = args[0]
        self.root.title("DnD Tools")
        self.settingsImage = tk.PhotoImage(file = "Images\SettingsImage.png")
        #Sets the size of the image to be smaller so that it will fix in the button for settings
        self.settingsImage = self.settingsImage.subsample(120, 120)

        #Sets up the pages
        createCharacterPage = CreateCharacterPage(self)
        battlePage = BattlePage(self)
        dicePage = DicePage(self)
        characterSheetPage = CharacterSheetPage(self)
        itemsAndSpellsPage = ItemsAndSpellsPage(self)
        addItemsAndSpellsPage = AddItemsAndSpellsPage(self)
        settingsPage = SettingsPage(self)

        #Creates a button Frame for all the tabs and a container for all the pages
        buttonFrame = tk.Frame(self)
        container = tk.Frame(self)
        buttonFrame.pack(side = "top", fill = "x", expand = False)
        container.pack(side = "top", fill = "both", expand = True)

        #Places the Pages in the container
        createCharacterPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        battlePage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        dicePage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        characterSheetPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        itemsAndSpellsPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        addItemsAndSpellsPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        settingsPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)

        #Creates the buttons that will be used to change to each page
        buttonCreateCharacterPage = tk.Button(buttonFrame, text = "Create character", command = createCharacterPage.lift)
        buttonBattlePage = tk.Button(buttonFrame, text = "Battle", command = battlePage.lift)
        buttonDicePage = tk.Button(buttonFrame, text = "Roll Dice", command = dicePage.lift)
        buttonCharacterSheetPage = tk.Button(buttonFrame, text = "View Characters", command = characterSheetPage.lift)
        buttonItemsAndSpellsPage = tk.Button(buttonFrame, text = "View items/spells", command = itemsAndSpellsPage.lift)
        buttonAddItemsAndSpellsPage = tk.Button(buttonFrame, text = "Add new items/spells", command = addItemsAndSpellsPage.lift)
        settingsButton = tk.Button(buttonFrame, image = self.settingsImage, command = settingsPage.lift)

        #Places the buttons in the button frame
        buttonCreateCharacterPage.pack(side = "left")
        buttonCharacterSheetPage.pack(side="left")
        buttonBattlePage.pack(side = "left")
        buttonDicePage.pack(side = "left")
        buttonItemsAndSpellsPage.pack(side = "left")
        buttonAddItemsAndSpellsPage.pack(side = "left")
        settingsButton.pack(side = "right")

        #Sets the createCharacterPage as the page shown when opening
        createCharacterPage.show()