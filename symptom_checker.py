from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from styles import apply_font
from languages import LANGUAGES
from kivy.app import App  # Add this import

class SymptomCheckerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Set background color
        with layout.canvas.before:
            Color(0.52, 0.66, 0.28, 1)  # Light green background
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

        # Bind the rectangle size to the layout size
        layout.bind(pos=self.update_rect, size=self.update_rect)

        # Symptom Input
        self.symptom_input = TextInput(
            hint_text="Describe your symptoms...",
            size_hint=(1, None),
            height=100,
            multiline=True,
            background_color=(1, 1, 1, 1),  # White background
            foreground_color=(0.07, 0.21, 0.14, 1)  # Dark green text
        )
        layout.add_widget(self.symptom_input)

        # Submit Button
        self.submit_button = Button(
            text="Submit",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        apply_font(self.submit_button)  # Apply custom font
        self.submit_button.bind(on_press=self.generate_diagnosis)
        layout.add_widget(self.submit_button)

        # Diagnosis Label
        self.diagnosis_label = Label(
            text="Your diagnosis will appear here.",
            font_size=14,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  # Dark green
        )
        apply_font(self.diagnosis_label)  # Apply custom font
        layout.add_widget(self.diagnosis_label)

        # Back Button
        self.back_button = Button(
            text="Back to Main Menu",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        apply_font(self.back_button)  # Apply custom font
        self.back_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def update_rect(self, instance, value):
        # Update the rectangle size and position when the layout changes
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def generate_diagnosis(self, instance):
        self.diagnosis_label.text = f"Based on your symptoms ({self.symptom_input.text}), you may have a common cold."

    def go_to_main_menu(self, instance):
        self.manager.current = "main_menu"

    def update_language(self):
        app = App.get_running_app()
        lang = app.current_language
        translations = LANGUAGES[lang]
        print(f"Updating SymptomCheckerScreen with language: {lang}")  # Debugging

        # Update the text of all widgets
        self.symptom_input.hint_text = translations["describe_symptoms"]
        self.submit_button.text = translations["submit"]
        self.diagnosis_label.text = translations["diagnosis"]
        self.back_button.text = translations["back_to_main_menu"]

        # Force refresh the UI
        self.symptom_input.canvas.ask_update()
        self.submit_button.canvas.ask_update()
        self.diagnosis_label.canvas.ask_update()
        self.back_button.canvas.ask_update()