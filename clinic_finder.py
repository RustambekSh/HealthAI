from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty
from styles import apply_font
import webbrowser
from kivy.app import App
from languages import LANGUAGES


class ClinicFinderScreen(Screen):
    # Add StringProperties for dynamic text
    map_text = StringProperty("Click the button below to find nearby clinics.")
    find_clinics_text = StringProperty("Find Clinics")
    back_text = StringProperty("Back to Main Menu")

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

        # Map Label
        self.map_label = Label(
            text=self.map_text,  # Bind to StringProperty
            font_size=14,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  # Dark green
        )
        apply_font(self.map_label)
        layout.add_widget(self.map_label)

        # Find Clinics Button
        self.find_clinics_button = Button(
            text=self.find_clinics_text,  # Bind to StringProperty
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        apply_font(self.find_clinics_button)
        self.find_clinics_button.bind(on_press=self.find_nearby_clinics)
        layout.add_widget(self.find_clinics_button)

        # Back Button
        self.back_button = Button(
            text=self.back_text,  # Bind to StringProperty
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        apply_font(self.back_button)
        self.back_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_language(self):
        """Update all text elements when language changes"""
        app = App.get_running_app()
        lang = app.current_language
        translations = LANGUAGES[lang]

        # Update StringProperties
        self.map_text = translations["find_nearby_clinics"]
        self.find_clinics_text = translations["find_clinics"]
        self.back_text = translations["back_to_main_menu"]

        # Force UI refresh
        self.map_label.canvas.ask_update()
        self.find_clinics_button.canvas.ask_update()
        self.back_button.canvas.ask_update()

    def find_nearby_clinics(self, instance):
        latitude = 41.2995  # Tashkent coordinates
        longitude = 69.2401
        google_maps_url = f"https://www.google.com/maps/search/clinics/@{latitude},{longitude},15z"
        webbrowser.open(google_maps_url)

    def go_to_main_menu(self, instance):
        self.manager.current = "main_menu"