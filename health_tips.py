import toga
from styles import create_button_style, create_label_style, create_box_style

class HealthTips:
    def __init__(self, main_window, on_back_click):
        self.main_window = main_window
        self.on_back_click = on_back_click

        # UI Elements
        self.tips_label = toga.Label(
            "1. Drink plenty of water.\n2. Wash your hands regularly.\n3. Get enough sleep.",
            style=create_label_style()
        )
        self.back_button = toga.Button(
            "Back to Main Menu",
            on_press=self.on_back_click,
            style=create_button_style()
        )

        # Layout
        self.box = toga.Box(
            children=[self.tips_label, self.back_button],
            style=create_box_style()
        )