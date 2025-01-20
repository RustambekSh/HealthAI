import toga
from toga.style import Pack
from styles import create_button_style, create_box_style, create_header_style, create_footer_style

class MainMenu:
    def __init__(self, main_window, on_ai_click, on_clinic_click, on_tips_click):
        self.main_window = main_window

        # Header (Program Name)
        self.header_label = toga.Label(
            "UzHealthAI",
            style=create_header_style()
        )

        # UI Elements
        self.ai_button = toga.Button(
            "AI Symptom Checker",
            on_press=on_ai_click,
            style=create_button_style()
        )
        self.clinic_button = toga.Button(
            "Find Clinics",
            on_press=on_clinic_click,
            style=create_button_style()
        )
        self.tips_button = toga.Button(
            "Health Tips",
            on_press=on_tips_click,
            style=create_button_style()
        )

        # Footer (Contact Info)
        self.footer_label = toga.Label(
            "Contact: info@uzhealthai.com | Support: support@uzhealthai.com",
            style=create_footer_style()
        )

        # Layout
        self.box = toga.Box(
            children=[
                self.header_label,
                self.ai_button,
                self.clinic_button,
                self.tips_button,
                self.footer_label
            ],
            style=create_box_style()
        )