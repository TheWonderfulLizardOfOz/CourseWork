import tkinter as tk
import random
from objects.background import Background

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class CreateCharacterPage(Page, Background):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Background.__init__(self)
        __tkvar = tk.StringVar(self)

        self.backgroundOptionList = [background[1] for background in self.getBackgroundList()]
        self.personalityOptionList = ["Select a background first"]
        self.idealOptionList = ["Select a background first"]
        self.bondOptionList = ["Select a background first"]
        self.flawOptionList = ["Select a background first"]

        self.personality = tk.StringVar(self)
        self.ideal = tk.StringVar(self)
        self.bond = tk.StringVar(self)
        self.flaw = tk.StringVar(self)

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

        randomBackgroundButton = tk.Button(self, text="s", command=lambda: self.randomOption(self.backgroundOptionList, self.background))
        randomBackgroundButton.place(relheight="0.06", relwidth="0.05", relx="0.42", rely="0.24")

        randomPersonalityButton = tk.Button(self, text = "s", command=lambda: self.randomOption(self.personalityOptionList, self.personality))
        randomPersonalityButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.42", rely = "0.3")

        randomIdealButton = tk.Button(self, text = "s", command=lambda: self.randomOption(self.idealOptionList, self.ideal))
        randomIdealButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.42", rely = "0.36")

        randomBondButton = tk.Button(self, text = "s", command=lambda: self.randomOption(self.bondOptionList, self.bond))
        randomBondButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.42", rely = "0.42")

        randomFlawButton = tk.Button(self, text = "s", command=lambda: self.randomOption(self.flawOptionList, self.flaw))
        randomFlawButton.place(relheight = "0.06", relwidth = 0.05, relx = "0.42", rely = "0.48")

        imageLabel = tk.Label(self, relief = "sunken", text = "Image")
        imageLabel.place(relheight = "0.45", relwidth = "0.45", relx = "0.53", rely = "0.03")

        uploadImageButton = tk.Button(self, text = "Upload Image")
        uploadImageButton.place(relheight = "0.06", relwidth = "0.225", relx = "0.53", rely = "0.48")

        randomImageButton = tk.Button(self, text = "Random Image")
        randomImageButton.place(relheight = "0.06", relwidth = "0.225", relx = "0.755", rely = "0.48")

        saveCharacterButton = tk.Button(self, text = "Save Character")
        saveCharacterButton.place(relheight = 0.18, relwidth = "0.16", relx = "0.31", rely = "0.03")

        nameLabel = tk.Label(self, relief = "groove", text = "Name")
        nameLabel.place(relheight = "0.06", relwidth = "0.06", relx = "0.02", rely = "0.03")

        raceLabel = tk.Label(self, relief = "groove", text = "Race")
        raceLabel.place(relheight = "0.06", relwidth = "0.06", relx = "0.02", rely = "0.09")

        classLabel = tk.Label(self, relief = "groove", text = "Class")
        classLabel.place(relheight = "0.06", relwidth = "0.06", relx = "0.02", rely = "0.15")

        nameEntry = tk.Entry(self)
        nameEntry.place(relheight = "0.06", relwidth = "0.15", relx = "0.08", rely = "0.03")

        self.raceOptionList = []
        raceOption = tk.OptionMenu(self, __tkvar, None, self.raceOptionList, command=None)
        raceOption.place(relheight = "0.06", relwidth = "0.15", relx = "0.08", rely = "0.09")

        self.classOptionList = []
        classOption = tk.OptionMenu(self, __tkvar, None, self.classOptionList, command=None)
        classOption.place(relheight = "0.06", relwidth = "0.15", relx = "0.08", rely = "0.15")

        randomNameButton = tk.Button(self, text = "s")
        randomNameButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.03")

        randomRaceButton = tk.Button(self, text = "s")
        randomRaceButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.09")

        randomClassButton = tk.Button(self, text = "s")
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

        randomStrengthButton = tk.Button(self, text = "s")
        randomStrengthButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.57")

        randomCharismaButton = tk.Button(self, text = "s")
        randomCharismaButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.63")

        randomWisdomButton = tk.Button(self, text = "s")
        randomWisdomButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.69")

        randomIntelligenceButton = tk.Button(self, text = "s")
        randomIntelligenceButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.75")

        randomDexterityButton = tk.Button(self, text = "s")
        randomDexterityButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.81")

        randomConstitutionButton = tk.Button(self, text = "s")
        randomConstitutionButton.place(relheight = "0.06", relwidth = "0.05", relx = "0.23", rely = "0.87")

        languagesLabel = tk.Label(self, relief = "groove", text = "Languages")
        languagesLabel.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.60")

        self.languageOptionList = []
        languageOptionOne = tk.OptionMenu(self, __tkvar, None, self.languageOptionList, command=None)
        languageOptionOne.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.66")

        languageOptionTwo = tk.OptionMenu(self, __tkvar, None, self.languageOptionList, command=None)
        languageOptionTwo.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.72")

        languageOptionThree = tk.OptionMenu(self, __tkvar, None, self.languageOptionList, command=None)
        languageOptionThree.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.78")

        languageOptionFour = tk.OptionMenu(self, __tkvar, None, self.languageOptionList, command=None)
        languageOptionFour.place(relheight = "0.06", relwidth = "0.15", relx = "0.32", rely = "0.84")

        skillLabel = tk.Label(self, relief = "groove", text = "Skills")
        skillLabel.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.57")

        self.skillOptionList = []
        skillOptionOne = tk.OptionMenu(self, __tkvar, None, self.skillOptionList, command=None)
        skillOptionOne.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.63")

        skillOptionTwo = tk.OptionMenu(self, __tkvar, None, self.skillOptionList, command=None)
        skillOptionTwo.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.69")

        skillOptionThree = tk.OptionMenu(self, __tkvar, None, self.skillOptionList, command=None)
        skillOptionThree.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.75")

        skillOptionFour = tk.OptionMenu(self, __tkvar, None, self.skillOptionList, command=None)
        skillOptionFour.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.81")

        skillOptionFive = tk.OptionMenu(self, __tkvar, None, self.skillOptionList, command=None)
        skillOptionFive.place(relheight = "0.06", relwidth = "0.21", relx = "0.53", rely = "0.87")

        toolLabel = tk.Label(self, relief = "groove", text = "Tools")
        toolLabel.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.57")

        self.toolOptionList = []
        toolOptionOne = tk.OptionMenu(self, __tkvar, None, self.toolOptionList, command=None)
        toolOptionOne.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.63")

        toolOptionTwo = tk.OptionMenu(self, __tkvar, None, self.toolOptionList, command=None)
        toolOptionTwo.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.69")

        toolOptionThree = tk.OptionMenu(self, __tkvar, None, self.toolOptionList, command=None)
        toolOptionThree.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.75")

        toolOptionFour = tk.OptionMenu(self, __tkvar, None, self.toolOptionList, command=None)
        toolOptionFour.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.81")

        toolOptionFive = tk.OptionMenu(self, __tkvar, None, self.toolOptionList, command=None)
        toolOptionFive.place(relheight = "0.06", relwidth = "0.21", relx = "0.77", rely = "0.87")

    def placeBackgroundFeatureWidgets(self):
        self.personality.set("Select an option")
        self.personalityOption = tk.OptionMenu(self, self.personality, *self.personalityOptionList, command=None)
        self.personalityOption.place(relheight="0.06", relwidth="0.25", relx="0.17", rely="0.3")

        self.ideal.set("Select an option")
        self.idealOption = tk.OptionMenu(self, self.ideal, *self.idealOptionList, command=None)
        self.idealOption.place(relheight=0.06, relwidth="0.25", relx="0.17", rely="0.36")

        self.bond.set("Select an option")
        self.bondOption = tk.OptionMenu(self, self.bond, *self.bondOptionList, command=None)
        self.bondOption.place(relheight="0.06", relwidth="0.25", relx="0.17", rely="0.42")

        self.flaw.set("Select an option")
        self.flawOption = tk.OptionMenu(self, self.flaw, *self.flawOptionList, command=None)
        self.flawOption.place(relheight="0.06", relwidth="0.25", relx="0.17", rely="0.48")

    def setLists(self):
        self.backgroundOptionList = [background[1] for background in self.getBackgroundList()]
        self.personalityOptionList = [feature[0] for feature in self.getFeatureList(self.personalityStatement)]
        self.idealOptionList = [feature[0] for feature in self.getFeatureList(self.idealStatement)]
        self.bondOptionList = [feature[0] for feature in self.getFeatureList(self.bondStatement)]
        self.flawOptionList = [feature[0] for feature in self.getFeatureList(self.flawStatement)]

    def backgroundUpdated(self, *args):
        self.newBackground = self.background.get()
        if self.newBackground == self.prevBackground:
            return
        else:
            self.prevBackground = self.newBackground

        self.openDB()
        self.cursor.execute("""SELECT backgroundID FROM background WHERE backgroundName = ?""", [args[0]])
        self.backgroundID = self.cursor.fetchall()
        self.backgroundID = self.backgroundID[0][0]
        self.closeDB()

        self.setStatements()
        self.setLists()

        self.personalityOption.destroy()
        self.idealOption.destroy()
        self.bondOption.destroy()
        self.flawOption.destroy()

        self.placeBackgroundFeatureWidgets()

    def randomOption(self, optionList, featureAttribute):
        featureAttribute.set(random.choice(optionList))
        if featureAttribute.get() in self.backgroundOptionList:
            self.backgroundUpdated(featureAttribute.get())

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
        self.settingsImage = self.settingsImage.subsample(120, 120)

        createCharacterPage = CreateCharacterPage(self)
        battlePage = BattlePage(self)
        dicePage = DicePage(self)
        characterSheetPage = CharacterSheetPage(self)
        itemsAndSpellsPage = ItemsAndSpellsPage(self)
        addItemsAndSpellsPage = AddItemsAndSpellsPage(self)
        settingsPage = SettingsPage(self)

        buttonFrame = tk.Frame(self)
        container = tk.Frame(self)
        buttonFrame.pack(side = "top", fill = "x", expand = False)
        container.pack(side = "top", fill = "both", expand = True)

        createCharacterPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        battlePage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        dicePage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        characterSheetPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        itemsAndSpellsPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        addItemsAndSpellsPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        settingsPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)

        buttonCreateCharacterPage = tk.Button(buttonFrame, text = "Create character", command = createCharacterPage.lift)
        buttonBattlePage = tk.Button(buttonFrame, text = "Battle", command = battlePage.lift)
        buttonDicePage = tk.Button(buttonFrame, text = "Roll Dice", command = dicePage.lift)
        buttonCharacterSheetPage = tk.Button(buttonFrame, text = "View Characters", command = characterSheetPage.lift)
        buttonItemsAndSpellsPage = tk.Button(buttonFrame, text = "Items/Spells", command = itemsAndSpellsPage.lift)
        buttonAddItemsAndSpellsPage = tk.Button(buttonFrame, text = "Add items/spells", command = addItemsAndSpellsPage.lift)
        settingsButton = tk.Button(buttonFrame, image = self.settingsImage, command = settingsPage.lift)

        buttonCreateCharacterPage.pack(side = "left")
        buttonBattlePage.pack(side = "left")
        buttonDicePage.pack(side = "left")
        buttonCharacterSheetPage.pack(side = "left")
        buttonItemsAndSpellsPage.pack(side = "left")
        buttonAddItemsAndSpellsPage.pack(side = "left")
        settingsButton.pack(side = "right")

        createCharacterPage.show()