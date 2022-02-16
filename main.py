from pages import *
from startPage import *
import tkinter as tk

#Creates and runs startPage
root = tk.Tk()
root.geometry("1080x607")
root.minsize(450, 300)
main = StartPage(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()

#If the startPage has been closed (which happens automatically when start button pressed)
#and start button clicked will open pages which will contain the GUI application
if main.startButtonClicked == True:
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x600")
    root.mainloop()