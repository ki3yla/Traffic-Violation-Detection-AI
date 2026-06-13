import customtkinter as ctk

from database import init_db
from login_screen import LoginScreen

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

init_db()

root = ctk.CTk()
root.geometry("1400x850")
root.title(
    "Traffic Violation Detection System"
)

LoginScreen(root)

root.mainloop()