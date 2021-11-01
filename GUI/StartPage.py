import tkinter as tk
from PIL import Image, ImageTk
import os.path

class StartPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.clicked = False

        self.image = Image.open(os.path.dirname(__file__) + "/../Images/SolidImageLogo.png")

        self.backgroundImage = ImageTk.PhotoImage(self.image)

        self.background = tk.Label(self, image = self.backgroundImage)
        self.background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        root.bind("<Enter>", self.resizeImage)
        root.bind("<Leave>", self.resizeImage)
        root.bind("<Configure>", lambda e: self.setClick(True))

    def resizeImage(self, event):
        if self.clicked == True:
            newWidth = event.widget.winfo_width()
            newHeight = event.widget.winfo_height()
            (newWidth, newHeight) = self.findIncreaseInProportions(newWidth, newHeight)
            self.resizedImage = ImageTk.PhotoImage(self.image.resize((newWidth, newHeight), Image.ANTIALIAS))
            self.background.configure(image = self.resizedImage)
            self.setClick(False)

    def findIncreaseInProportions(self, newWidth, newHeight):
        if int(newWidth/16) > int(newHeight/9):
            newProportion = int(newHeight/9)
        else:
            newProportion = int(newWidth/16)
        newWidth = 16*newProportion
        newHeight = 9*newProportion
        return (newWidth, newHeight)

    def setClick(self, value):
        self.clicked = value

root = tk.Tk()
root.geometry("800x450")
main = StartPage(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()