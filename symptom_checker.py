from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class SymptomCheckerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Symptom Input
        self.symptom_input = TextInput(
            hint_text="Describe your symptoms...",
            size_hint=(1, None),
            height=100,
            multiline=True
        )
        layout.add_widget(self.symptom_input)

        # Submit Button
        self.submit_button = Button(
            text="Submit",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.28, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        self.submit_button.bind(on_press=self.generate_diagnosis)
        layout.add_widget(self.submit_button)

        # Diagnosis Label
        self.diagnosis_label = Label(
            text="Your diagnosis will appear here.",
            font_size=14,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  # Dark green
        )
        layout.add_widget(self.diagnosis_label)

        # Back Button
        self.back_button = Button(
            text="Back to Main Menu",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.28, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        self.back_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def generate_diagnosis(self, instance):
        self.diagnosis_label.text = f"Based on your symptoms ({self.symptom_input.text}), you may have a common cold."

    def go_to_main_menu(self, instance):
        self.manager.current = "main_menu"