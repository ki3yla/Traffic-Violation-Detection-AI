import customtkinter as ctk
from PIL import Image
import os

from dashboard_screen import DashboardScreen

class LoginScreen:

    def __init__(self, root):

        self.root = root

        self.create_background()

        self.card = ctk.CTkFrame(
            root,
            width=500,
            height=550,
            corner_radius=25
        )

        self.card.place(
            relx=0.5,
            rely=1.2,
            anchor="center"
        )

        ctk.CTkLabel(
            self.card,
            text="🚦",
            font=("Arial", 60)
        ).pack(pady=(25,0))

        ctk.CTkLabel(
            self.card,
            text="Traffic Violation\nDetection System",
            font=("Arial", 28, "bold")
        ).pack(pady=15)

        ctk.CTkLabel(
            self.card,
            text="Authority Login Portal",
            font=("Arial", 16)
        ).pack(pady=5)

        self.username = ctk.CTkEntry(
            self.card,
            width=340,
            height=45,
            placeholder_text="Username"
        )

        self.username.pack(pady=15)

        self.password = ctk.CTkEntry(
            self.card,
            width=340,
            height=45,
            placeholder_text="Password",
            show="*"
        )

        self.password.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.card,
            text=""
        )

        self.status_label.pack(pady=10)

        self.login_btn = ctk.CTkButton(
            self.card,
            text="Login",
            width=340,
            height=50,
            command=self.login
        )

        self.login_btn.pack(pady=20)

        self.pos_y = 1.2
        self.animate_card()

    def create_background(self):

        if os.path.exists(
            "assets/traffic_bg.jpg"
        ):

            image = ctk.CTkImage(
                light_image=Image.open(
                    "assets/traffic_bg.jpg"
                ),
                dark_image=Image.open(
                    "assets/traffic_bg.jpg"
                ),
                size=(1400,850)
            )

            bg = ctk.CTkLabel(
                self.root,
                image=image,
                text=""
            )

            bg.image = image

            bg.place(
                relwidth=1,
                relheight=1
            )

        else:

            self.root.configure(
                fg_color="#0B1120"
            )

    def animate_card(self):

        if self.pos_y > 0.5:

            self.pos_y -= 0.02

            self.card.place(
                relx=0.5,
                rely=self.pos_y,
                anchor="center"
            )

            self.root.after(
                10,
                self.animate_card
            )

    def login(self):

        username = self.username.get()
        password = self.password.get()

        if not username:

            self.status_label.configure(
                text="Please enter username",
                text_color="red"
            )

            return

        if not password:

            self.status_label.configure(
                text="Please enter password",
                text_color="red"
            )

            return

        self.status_label.configure(
            text="Login Successful",
            text_color="green"
        )

        self.root.after(
            800,
            self.open_dashboard
        )

    def open_dashboard(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        DashboardScreen(
            self.root
        )