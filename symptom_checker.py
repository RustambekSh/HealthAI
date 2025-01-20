import toga
from styles import create_button_style, create_label_style, create_box_style

class SymptomChecker:
    def __init__(self, main_window, on_back_click):
        self.main_window = main_window
        self.user_input = ""
        self.on_back_click = on_back_click

        # UI Elements
        self.symptom_input = toga.TextInput(
            placeholder="Describe your symptoms...",
            style=create_label_style()
        )
        self.submit_button = toga.Button(
            "Submit",
            on_press=self.generate_diagnosis,
            style=create_button_style()
        )
        self.diagnosis_label = toga.Label(
            "Your diagnosis will appear here.",
            style=create_label_style()
        )
        self.back_button = toga.Button(
            "Back to Main Menu",
            on_press=self.on_back_click,
            style=create_button_style()
        )

        # Layout
        self.box = toga.Box(
            children=[self.symptom_input, self.submit_button, self.diagnosis_label, self.back_button],
            style=create_box_style()
        )

    def generate_diagnosis(self, widget):
        self.user_input = self.symptom_input.value
        # Simulate AI diagnosis (replace with actual AI integration)
        self.diagnosis_label.text = f"Based on your symptoms ({self.user_input}), you may have a common cold."