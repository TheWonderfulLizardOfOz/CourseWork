import tkinter as tk
from PIL import Image, ImageTk
import os.path

class StartPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.startButtonClicked = False
        self.clicked = False
        self.root = args[0]

        self.image = Image.open(os.path.dirname(__file__) + "/../Images/SolidImageLogo.png")

        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.background = tk.Label(self.root, image = self.backgroundImage)
        self.startButton = tk.Button(self.root, text = "Start", command = self.start)
        self.instructionsButton = tk.Button(self.root, text = "Instructions", command = self.instructions)

        self.background.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        self.startButton.place(relx = 0.25, rely = 0.75, relwidth = 0.15, relheight = 0.05)
        self.instructionsButton.place(relx = 0.60, rely = 0.75, relwidth = 0.15, relheight = 0.05)

        self.root.bind("<Enter>", self.resizeImage)
        self.root.bind("<Leave>", self.resizeImage)
        self.root.bind("<Configure>", lambda e: self.setClick(True))

    def resizeImage(self, event):
        if self.clicked == True:
            newWidth = event.widget.winfo_width()
            newHeight = event.widget.winfo_height()
            (newWidth, newHeight) = self.findIncreaseInProportions(newWidth, newHeight)
            self.resizedImage = ImageTk.PhotoImage(self.image.resize((newWidth, newHeight), Image.ANTIALIAS))
            self.background.configure(image = self.resizedImage)

            self.setClick(False)

    def findIncreaseInProportions(self, newWidth, newHeight):
        widthSF = int(newWidth/16)
        heightSF = int(newHeight/9)
        if widthSF > heightSF:
            newProportion = heightSF
        else:
            newProportion = widthSF
        newWidth = 16*newProportion
        newHeight = 9*newProportion
        return (newWidth, newHeight)

    def setClick(self, value):
        self.clicked = value

    def start(self):
        self.startButtonClicked = True
        self.root.destroy()

    def instructions(self):
        self.instructionsPage = tk.Toplevel(self.root)