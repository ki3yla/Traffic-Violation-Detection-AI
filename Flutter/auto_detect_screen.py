import customtkinter as ctk
import threading

from roboflow_service import detect_image

class AutoDetectScreen:

    def __init__(
        self,
        parent,
        image_path,
        callback=None
    ):

        self.callback = callback
        self.image_path = image_path

        self.window = ctk.CTkToplevel(parent)
        self.window.geometry("700x500")
        self.window.title("AI Detection")

        ctk.CTkLabel(
            self.window,
            text="🤖 AI Traffic Violation Detection",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        self.status_label = ctk.CTkLabel(
            self.window,
            text="Preparing Detection..."
        )

        self.status_label.pack(pady=10)

        self.progress = ctk.CTkProgressBar(
            self.window,
            width=500
        )

        self.progress.pack(pady=10)

        self.progress.set(0)

        self.result_box = ctk.CTkTextbox(
            self.window,
            width=550,
            height=180
        )

        self.result_box.pack(pady=20)

        self.start_detection()

    def start_detection(self):

        thread = threading.Thread(
            target=self.run_detection
        )

        thread.daemon = True
        thread.start()

    def run_detection(self):

        try:

            self.progress.set(0.2)
            self.status_label.configure(
                text="Uploading Image..."
            )

            result = detect_image(
                self.image_path
            )

            self.progress.set(0.6)

            predictions = result.get(
                "predictions",
                []
            )

            if predictions:

                prediction = predictions[0]

                violation = prediction.get(
                    "class",
                    "Unknown"
                )

                confidence = round(
                    prediction.get(
                        "confidence",
                        0
                    ) * 100,
                    2
                )

                self.progress.set(1)

                self.status_label.configure(
                    text="Detection Complete"
                )

                self.result_box.insert(
                    "end",
                    f"""
Violation Detected

Type:
{violation}

Confidence:
{confidence}%

Status:
READY FOR SUBMISSION
"""
                )

                if self.callback:

                    self.callback(
                        violation,
                        confidence
                    )

            else:

                self.progress.set(1)

                self.result_box.insert(
                    "end",
                    """
No Violation Detected
"""
                )

        except Exception as e:

            self.result_box.insert(
                "end",
                f"""
Detection Failed

{str(e)}
"""
            )