from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Header (Program Name)
        self.header_label = Label(
            text="UzHealthAI",
            font_size=24,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  # Dark green
        )
        layout.add_widget(self.header_label)

        # Buttons
        self.ai_button = Button(
            text="AI Symptom Checker",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.28, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        self.ai_button.bind(on_press=self.go_to_symptom_checker)
        layout.add_widget(self.ai_button)

        self.clinic_button = Button(
            text="Find Clinics",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.28, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        self.clinic_button.bind(on_press=self.go_to_clinic_finder)
        layout.add_widget(self.clinic_button)

        self.tips_button = Button(
            text="Health Tips",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.28, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        self.tips_button.bind(on_press=self.go_to_health_tips)
        layout.add_widget(self.tips_button)

        # Footer (Contact Info)
        self.footer_label = Label(
            text="Contact: info@uzhealthai.com | Support: support@uzhealthai.com",
            font_size=12,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  # Dark green
        )
        layout.add_widget(self.footer_label)

        self.add_widget(layout)

    def go_to_symptom_checker(self, instance):
        self.manager.current = "symptom_checker"

    def go_to_clinic_finder(self, instance):
        self.manager.current = "clinic_finder"

    def go_to_health_tips(self, instance):
        self.manager.current = "health_tips"