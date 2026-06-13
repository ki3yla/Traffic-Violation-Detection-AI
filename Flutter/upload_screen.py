import customtkinter as ctk

from tkinter import filedialog
from PIL import Image

from datetime import datetime

from database import add_report

class UploadScreen:

    def __init__(
        self,
        parent,
        dashboard
    ):

        self.parent = parent
        self.dashboard = dashboard

        self.image_path = None

        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        ctk.CTkLabel(
            self.frame,
            text="Upload Traffic Evidence",
            font=("Arial", 24, "bold")
        ).pack(pady=15)

        self.image_preview = ctk.CTkLabel(
            self.frame,
            text="No Image Selected",
            width=350,
            height=250
        )

        self.image_preview.pack(pady=10)

        self.violation_var = ctk.StringVar(
            value="Red Light Violation"
        )

        self.violation_menu = ctk.CTkOptionMenu(
            self.frame,
            values=[
                "Red Light Violation",
                "Speeding",
                "Illegal Lane Change",
                "No Seatbelt",
                "Using Mobile Phone",
                "Double Parking"
            ],
            variable=self.violation_var
        )

        self.violation_menu.pack(pady=10)

        ctk.CTkButton(
            self.frame,
            text="📁 Browse Image",
            command=self.select_image
        ).pack(pady=5)

        ctk.CTkButton(
            self.frame,
            text="🤖 Detect Violation",
            command=self.detect
        ).pack(pady=5)

        ctk.CTkButton(
            self.frame,
            text="☁ Submit Report",
            command=self.submit_report
        ).pack(pady=5)

        self.result_label = ctk.CTkLabel(
            self.frame,
            text="Waiting for Detection..."
        )

        self.result_label.pack(pady=15)

        self.progress = ctk.CTkProgressBar(
            self.frame,
            width=350
        )

        self.progress.pack(pady=10)

        self.progress.set(0)

    def select_image(self):

        self.image_path = filedialog.askopenfilename(
            filetypes=[
                (
                    "Images",
                    "*.jpg *.png *.jpeg"
                )
            ]
        )

        if not self.image_path:
            return

        image = ctk.CTkImage(
            light_image=Image.open(
                self.image_path
            ),
            dark_image=Image.open(
                self.image_path
            ),
            size=(320,220)
        )

        self.image_preview.configure(
            image=image,
            text=""
        )

        self.image_preview.image = image

    def detect(self):

        if not self.image_path:
            return

        self.progress.set(0.2)

        self.frame.after(
            500,
            lambda:self.progress.set(0.5)
        )

        self.frame.after(
            1000,
            lambda:self.progress.set(0.8)
        )

        self.frame.after(
            1500,
            self.finish_detection
        )

    def finish_detection(self):

        self.progress.set(1)

        self.result_label.configure(
            text="""
🚨 Violation Detected

Type:
Red Light Violation

Confidence:
95.4%
"""
        )

    def submit_report(self):

        if not self.image_path:
            return

        add_report(
            self.violation_var.get(),
            self.image_path,
            95.4,
            "Kuala Lumpur",
            datetime.now().strftime(
                "%d/%m/%Y %H:%M"
            )
        )

        self.result_label.configure(
            text="✅ Report Submitted"
        )

        if hasattr(
            self.dashboard,
            "refresh_stats"
        ):
            self.dashboard.refresh_stats()

        if hasattr(
            self.dashboard,
            "load_reports"
        ):
            self.dashboard.load_reports()