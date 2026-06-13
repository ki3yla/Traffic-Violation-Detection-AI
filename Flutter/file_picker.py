from tkinter import filedialog

def pick_image():
    return filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.jpg *.png *.jpeg")
        ]
    )