import customtkinter as ctk
from datetime import datetime
from tkinter import filedialog
from roboflow import Roboflow  # Import Roboflow client
from PIL import Image

class DashboardScreen:

    def __init__(self, root):
        self.root = root

        # Initialize file tracking variable
        self.selected_file_path = None
        self.current_violations = []

        # --- ROBOFLOW CONFIGURATION ---
        # Replace these with your actual Roboflow credentials
        self.ROBOFLOW_API_KEY = "gORy5nDjgvI51ufllEGB"
        self.PROJECT_ID = "traffic-violation-detection-hb0we"
        self.MODEL_VERSION = 1
        # ------------------------------

        self.main_frame = ctk.CTkFrame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.create_sidebar()
        self.create_content()
        self.update_clock()

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self.main_frame, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(
            self.sidebar, text="🚦 TVDS", font=("Arial", 28, "bold")
        ).pack(pady=30)

        ctk.CTkButton(
            self.sidebar,
            text="📊 Dashboard",
            width=180,
            command=self.show_dashboard,
        ).pack(pady=8)
        ctk.CTkButton(
            self.sidebar,
            text="📤 Upload Evidence",
            width=180,
            command=self.show_upload,
        ).pack(pady=8)
        ctk.CTkButton(
            self.sidebar,
            text="🤖 AI Detection",
            width=180,
            command=self.show_detection,
        ).pack(pady=8)
        ctk.CTkButton(
            self.sidebar,
            text="📜 History",
            width=180,
            command=self.show_history,
        ).pack(pady=8)
        ctk.CTkButton(
            self.sidebar,
            text="📍 Locations",
            width=180,
            command=self.show_locations,
        ).pack(pady=8)

    def create_content(self):
        self.content = ctk.CTkScrollableFrame(self.main_frame)
        self.content.pack(
            side="left", fill="both", expand=True, padx=15, pady=15
        )

        self.create_header()
        self.create_stats()
        self.create_upload_section()
        self.create_history_section()
        self.create_location_section()
        self.create_analytics_section()

    def create_header(self):
        header = ctk.CTkFrame(self.content)
        header.pack(fill="x", pady=10)

        ctk.CTkLabel(
            header,
            text="Traffic Violation Monitoring Center",
            font=("Arial", 30, "bold"),
        ).pack(side="left", padx=15)

        self.clock_label = ctk.CTkLabel(header, text="")
        self.clock_label.pack(side="right", padx=15)

    def create_stats(self):
        frame = ctk.CTkFrame(self.content)
        frame.pack(fill="x", pady=10)

        self.create_card(frame, "🚗 Total Reports", "0")
        self.create_card(frame, "🚨 Today", "0")
        self.create_card(frame, "🤖 AI Status", "Online")
        self.create_card(frame, "☁ Sync", "Active")

    def create_card(self, parent, title, value):
        card = ctk.CTkFrame(parent, width=220, height=120)
        card.pack(side="left", padx=10, pady=10)

        ctk.CTkLabel(card, text=title).pack(pady=10)
        ctk.CTkLabel(card, text=value, font=("Arial", 28, "bold")).pack()

    def create_upload_section(self):
        section = ctk.CTkFrame(self.content)
        section.pack(fill="x", pady=15)

        left = ctk.CTkFrame(section)
        left.pack(side="left", fill="both", expand=True, padx=10)

        ctk.CTkLabel(
            left, text="Upload Evidence", font=("Arial", 22, "bold")
        ).pack(pady=10)

        self.preview_label = ctk.CTkLabel(
            left, text="No Image Selected", width=300, height=180
        )
        self.preview_label.pack(pady=10)

        ctk.CTkButton(
            left, text="Browse Image", command=self.browse_image
        ).pack(pady=5)
        ctk.CTkButton(
            left, text="Detect Violation", command=self.detect_violation
        ).pack(pady=5)
        ctk.CTkButton(
            left, text="Submit Report", command=self.submit_report
        ).pack(pady=5)

        right = ctk.CTkFrame(section)
        right.pack(side="left", fill="both", expand=True, padx=10)

        ctk.CTkLabel(
            right, text="AI Detection Result", font=("Arial", 22, "bold")
        ).pack(pady=10)

        self.result_box = ctk.CTkTextbox(right, height=220)
        self.result_box.pack(fill="both", expand=True, padx=10, pady=10)
        self.result_box.insert("end", "Waiting for Detection...")

    def create_history_section(self):
        frame = ctk.CTkFrame(self.content)
        frame.pack(fill="x", pady=15)

        ctk.CTkLabel(
            frame, text="Recent Violations", font=("Arial", 22, "bold")
        ).pack(anchor="w", padx=15)

        self.history_box = ctk.CTkTextbox(frame, height=180)
        self.history_box.pack(fill="x", padx=15, pady=10)
        self.history_box.insert("end", "No reports available.")

    def create_location_section(self):
        frame = ctk.CTkFrame(self.content)
        frame.pack(fill="x", pady=15)

        ctk.CTkLabel(
            frame, text="Violation Hotspots", font=("Arial", 22, "bold")
        ).pack(anchor="w", padx=15)

        locations = [
            "📍 Kuala Lumpur - 12 Cases",
            "📍 Petaling Jaya - 8 Cases",
            "📍 Bangsar - 5 Cases",
            "📍 Shah Alam - 4 Cases",
        ]

        for location in locations:
            ctk.CTkLabel(frame, text=location, font=("Arial", 16)).pack(
                anchor="w", padx=20, pady=3
            )

    def create_analytics_section(self):
        frame = ctk.CTkFrame(self.content)
        frame.pack(fill="x", pady=15)

        ctk.CTkLabel(frame, text="Analytics", font=("Arial", 22, "bold")).pack(
            pady=10
        )

        analytics = ctk.CTkTextbox(frame, height=150)
        analytics.pack(fill="x", padx=15, pady=10)

        analytics.insert(
            "end",
            "Red Light Violation   ██████████████ 25\n"
            "Speeding               ███████████ 18\n"
            "No Seatbelt            ███████ 12\n"
            "Phone Usage            █████ 8\n"
            "Double Parking         ███ 4",
        )

    def browse_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.png *.jpeg")]
        )

        if file_path:
            self.selected_file_path = file_path  # Keep track of file path
            
            try:
                # Open the selected image
                your_image = Image.open(file_path)
                
                # Create a CTkImage object (matching the UI layout dimensions 300x180)
                self.preview_img = ctk.CTkImage(
                    light_image=your_image, 
                    dark_image=your_image, 
                    size=(300, 180)
                )
                
                # Display the image and clear out the old placeholder text
                self.preview_label.configure(image=self.preview_img, text="")
                
            except Exception as e:
                self.preview_label.configure(text=f"Error loading image: {e}")

    def detect_violation(self):
        self.result_box.delete("1.0", "end")

        # Guard clause if user hasn't uploaded an image yet
        if not self.selected_file_path:
            self.result_box.insert("end", "Error: Please select an image first.")
            return

        self.result_box.insert("end", "Analyzing image with Roboflow AI...\n")
        self.root.update_idletasks()  # Forces UI to display the text instantly

        try:
            # Initialize Roboflow Client
            rf = Roboflow(api_key=self.ROBOFLOW_API_KEY)
            project = rf.project(self.PROJECT_ID)
            model = project.version(self.MODEL_VERSION).model

            # Perform prediction on the local image file
            prediction = model.predict(self.selected_file_path, confidence=40)
            predictions_list = prediction.json().get("predictions", [])

            # === VISUAL PREVIEW GENERATION ===
            try:
                # 1. Saves a temporary file with the prediction boxes drawn on top
                prediction.save("predicted_image.jpg")
                
                # 2. Reload the newly saved image using PIL
                detected_img = Image.open("predicted_image.jpg")
                
                # 3. Re-wrap it in a CTkImage for CustomTkinter
                self.preview_img = ctk.CTkImage(
                    light_image=detected_img, 
                    dark_image=detected_img, 
                    size=(300, 180)
                )
                
                # 4. Update the UI layout container to show the image instead of text
                self.preview_label.configure(image=self.preview_img, text="")
            except Exception as img_err:
                print(f"Error rendering visual bounding boxes: {img_err}")

            self.result_box.delete("1.0", "end")

            if not predictions_list:
                self.current_violations = [] # Clear violations list if clean
                self.result_box.insert(
                    "end", "Analysis Complete:\n\nNo violations detected."
                )
                return

            # ================================================================
            # STEP 2 INTEGRATION: DYNAMICALLY SAVE DETECTIONS FOR REPORTING
            # ================================================================
            self.result_box.insert("end", "Violations Detected:\n\n")
            
            # Reset the list so previous images don't leak into new submissions
            self.current_violations = [] 
            
            for index, pred in enumerate(predictions_list, 1):
                label = pred.get("class", "Unknown")
                confidence = pred.get("confidence", 0.0) * 100

                self.result_box.insert(
                    "end",
                    f"[{index}] Type: {label.title()}\n"
                    f"    Confidence: {confidence:.1f}%\n\n",
                )
                
                # Append formatted violation names to our global tracker
                self.current_violations.append(label.title())
            # ================================================================

        except Exception as e:
            self.result_box.delete("1.0", "end")
            self.result_box.insert(
                "end", f"API Connection Error:\n\n{str(e)}\n\nCheck your API Key."
            )

    def submit_report(self):
        # 1. Guard clause if they haven't run a detection yet
        if not self.selected_file_path or not hasattr(self, 'current_violations'):
            self.result_box.insert("end", "\nError: Nothing to submit. Run detection first.")
            return

        # 2. Guard clause if the image was clean (no violations found)
        if not self.current_violations:
            self.result_box.insert("end", "\nNotification: No violations found to report.")
            return

        # 3. Clear out the initial text block placeholder if it's still there
        current_history_text = self.history_box.get("1.0", "end-1c")
        if "No reports available." in current_history_text:
            self.history_box.delete("1.0", "end")

        # 4. Generate timestamp and format the real entries
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Combine unique violations discovered into a clean string (e.g., "No-Helmet, Motorcycle")
        unique_violations = ", ".join(list(set(self.current_violations)))
        
        # 5. Append the real information down into your Recent Violations panel
        report_entry = f"📝 [{timestamp}] {unique_violations} - Submitted Successfully\n"
        self.history_box.insert("end", report_entry)
        
        # 6. Notify the user in the AI box that it's sent!
        self.result_box.insert("end", "\n✅ Report successfully submitted to database history!")  # You can later make this dynamic too!

    def update_clock(self):
        self.clock_label.configure(
            text=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )
        self.root.after(1000, self.update_clock)

    def show_dashboard(self):
        self.content._parent_canvas.yview_moveto(0)

    def show_upload(self):
        self.content._parent_canvas.yview_moveto(0.20)

    def show_detection(self):
        self.content._parent_canvas.yview_moveto(0.20)

    def show_history(self):
        self.content._parent_canvas.yview_moveto(0.55)

    def show_locations(self):
        self.content._parent_canvas.yview_moveto(0.80)