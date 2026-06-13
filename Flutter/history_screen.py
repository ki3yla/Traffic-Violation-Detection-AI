import tkinter as tk
from report_data import global_reports

class HistoryScreen:

    def __init__(self, root):

        self.window = tk.Toplevel(root)
        self.window.title("Submission History")

        listbox = tk.Listbox(
            self.window,
            width=80,
            height=20
        )

        listbox.pack()

        for report in global_reports:

            listbox.insert(
                tk.END,
                f"{report.violation_type} - {report.timestamp}"
            )