from pages import *
from startPage import *

root = tk.Tk()
root.geometry("800x450")
root.minsize(450, 300)
main = StartPage(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()

if main.startButtonClicked == True:
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x600")
    root.mainloop()