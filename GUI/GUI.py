import tkinter as tk
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class CreateCharacterPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

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

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        createCharacterPage = CreateCharacterPage(self)
        battlePage = BattlePage(self)
        dicePage = DicePage(self)
        characterSheetPage = CharacterSheetPage(self)
        itemsAndSpellsPage = ItemsAndSpellsPage(self)
        addItemsAndSpellsPage = AddItemsAndSpellsPage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side = "top", fill = "x", expand = False)
        container.pack(side = "top", fill = "both", expand = True)

        createCharacterPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        battlePage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        dicePage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        characterSheetPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        itemsAndSpellsPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)
        addItemsAndSpellsPage.place(in_ = container, x = 0, y = 9, relwidth = 1, relheight = 1)

        buttonCreateCharacterPage = tk.Button(buttonframe, text = "Create character", command = createCharacterPage.lift)
        buttonBattlePage = tk.Button(buttonframe, text = "Battle", command = battlePage.lift)
        buttonDicePage = tk.Button(buttonframe, text = "Roll Dice", command = dicePage.lift)
        buttonCharacterSheetPage = tk.Button(buttonframe, text = "View Characters", command = characterSheetPage.lift)
        buttonItemsAndSpellsPage = tk.Button(buttonframe, text = "Items/Spells", command = itemsAndSpellsPage.lift)
        buttonAddItemsAndSpellsPage = tk.Button(buttonframe, text = "Add items/spells", command = addItemsAndSpellsPage.lift)

        buttonCreateCharacterPage.pack(side = "left")
        buttonBattlePage.pack(side = "left")
        buttonDicePage.pack(side = "left")
        buttonCharacterSheetPage.pack(side = "left")
        buttonItemsAndSpellsPage.pack(side = "left")
        buttonAddItemsAndSpellsPage.pack(side = "left")

        createCharacterPage.show()

root = tk.Tk()
main = MainView(root)
main.pack(side = "top", fill = "both", expand = True)
root.wm_geometry("1000x600")
root.mainloop()