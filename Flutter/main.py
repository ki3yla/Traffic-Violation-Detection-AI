from tkinter import Tk
from login_screen import LoginScreen

root = Tk()
root.title("Traffic Violation System")
root.geometry("800x600")

app = LoginScreen(root)

root.mainloop()