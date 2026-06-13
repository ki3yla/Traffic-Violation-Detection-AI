import tkinter as tk

class LocationScreen:

    def __init__(self, root):

        self.window = tk.Toplevel(root)
        self.window.title("Violation Locations")

        locations = [
            "Jalan Tun Razak, KL",
            "Federal Highway, PJ",
            "Jalan Bangsar"
        ]

        for location in locations:
            tk.Label(
                self.window,
                text=location
            ).pack(pady=5)