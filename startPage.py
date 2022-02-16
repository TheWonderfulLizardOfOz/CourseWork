import tkinter as tk
from PIL import Image, ImageTk

class StartPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.root = args[0]
        self.root.title("Start menu")
        #Attribute that is used to check if the start button was clicked
        self.startButtonClicked = False
        #Attribute that is used to check if the mouse has been clicked
        self.clicked = False
        #Creates an object of the Instructions class that will be used to make instructions visible
        self.instructionsWindow = Instructions()
        self.instructionsWindow.withdraw()

        self.image = Image.open("Images\SolidImageLogo.png")

        #Image is made compatible with tkinter and the placed in background label
        #Widgets are also created here
        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.background = tk.Label(self.root, image = self.backgroundImage)
        self.startButton = tk.Button(self.root, text = "Start", command = self.start)
        self.instructionsButton = tk.Button(self.root, text = "Instructions", command = self.showInstructions)

        #Places widgets
        self.background.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        self.startButton.place(relx = 0.25, rely = 0.75, relwidth = 0.15, relheight = 0.05)
        self.instructionsButton.place(relx = 0.60, rely = 0.75, relwidth = 0.15, relheight = 0.05)

        #Calls resizeImage method every time the cursor leaves or enters the window
        self.root.bind("<Enter>", self.resizeImage)
        self.root.bind("<Leave>", self.resizeImage)
        #Calls setClick when widget is resized
        self.root.bind("<Configure>", lambda e: self.setClick(True))
        #All the events are requires as with just the configure event there are performance issues

    def resizeImage(self, event):
        #Checks if image has been resized before running
        if self.clicked == True:
            #Changes size of image based of window size
            newWidth = event.widget.winfo_width()
            newHeight = event.widget.winfo_height()
            (newWidth, newHeight) = self.findIncreaseInProportions(newWidth, newHeight)
            self.resizedImage = ImageTk.PhotoImage(self.image.resize((newWidth, newHeight), Image.ANTIALIAS))
            self.background.configure(image = self.resizedImage)
            #sets click to False so that the function won't run again unless clicked
            self.setClick(False)

    #Finds the change in proportions so that the image always keeps the same dimensions
    #Uses the smallest change to ensure that it fits
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

    #Runs when the start button is pressed, sets startButtonClicked to True so that the
    # program in main knows to run the tkinter application that holds the pages
    def start(self):
        self.startButtonClicked = True
        #Destroys the window
        self.root.destroy()

    def showInstructions(self):
        #Destroys previous instance of instructionsWindow as to not have multiple instances of instructionsWindow
        self.instructionsWindow.destroy()
        self.instructionsWindow = Instructions()

#Toplevel is a window that goes over the top of the main application
class Instructions(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Instructions")
        self.textBox = tk.Text(self)
        self.scrollBar = tk.Scrollbar(self, command = self.textBox.yview)
        # Binds the scroll bar to the textBox
        self.textBox.config(yscrollcommand = self.scrollBar.set, wrap = tk.WORD)

        #Places the scrollBar on the right hand side and covers the vertical axis
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textBox.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

        text = "hello "
        self.textBox.insert(tk.END, 1000*text)
        #Makes it so that the text in the text box can't be edited
        self.textBox.config(state = "disabled")