import tkinter as tk
from PIL import Image, ImageTk

class StartPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.root = args[0]
        self.root.title("Start menu")
        self.startButtonClicked = False
        self.clicked = False
        self.instructionsWindow = Instructions()
        self.instructionsWindow.withdraw()

        self.image = Image.open("Images\SolidImageLogo.png")

        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.background = tk.Label(self.root, image = self.backgroundImage)
        self.startButton = tk.Button(self.root, text = "Start", command = self.start)
        self.instructionsButton = tk.Button(self.root, text = "Instructions", command = self.showInstructions)

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

    def showInstructions(self):
        self.instructionsWindow.destroy()
        self.instructionsWindow = Instructions()

class Instructions(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Instructions")
        self.textBox = tk.Text(self)
        self.scrollBar = tk.Scrollbar(self, command = self.textBox.yview)
        self.textBox.config(yscrollcommand = self.scrollBar.set, wrap = tk.WORD)

        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textBox.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

        text = "hello "
        self.textBox.insert(tk.END, 1000*text)
        self.textBox.config(state = "disabled")