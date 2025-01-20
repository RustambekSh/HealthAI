from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from styles import apply_font
from languages import LANGUAGES
from kivy.app import App  # Add this import

class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        layout = BoxLayout(orientation="vertical")

        # Set background color
        with layout.canvas.before:
            Color(0.52, 0.66, 0.28, 1)  # Light green background
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

        # Bind the rectangle size to the layout size
        layout.bind(pos=self.update_rect, size=self.update_rect)

        # App Name Label
        self.app_name_label = Label(
            text="UzHealthAI",  # Default text
            font_size=48,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  # Dark green
        )
        apply_font(self.app_name_label)  # Apply custom font
        layout.add_widget(self.app_name_label)

        self.add_widget(layout)

        # Schedule the transition to the main menu after 4 seconds
        Clock.schedule_once(self.go_to_main_menu, 4)

    def update_rect(self, instance, value):
        # Update the rectangle size and position when the layout changes
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_main_menu(self, dt):
        # Transition to the main menu screen
        self.manager.current = "main_menu"

    def update_language(self):
        # Update the app name based on the selected language
        app = App.get_running_app()
        lang = app.current_language
        translations = LANGUAGES[lang]
        self.app_name_label.text = translations["app_name"]