from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from styles import apply_font
import webbrowser

class ClinicFinderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

      
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        
        with layout.canvas.before:
            Color(0.52, 0.66, 0.28, 1)  
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

        
        layout.bind(pos=self.update_rect, size=self.update_rect)
        self.map_label = Label(
            text="Click the button below to find nearby clinics.",
            font_size=14,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  
        )
        apply_font(self.map_label)  
        layout.add_widget(self.map_label)

        
        self.find_clinics_button = Button(
            text="Find Clinics",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),  
            color=(1, 1, 1, 1),  
            bold=True
        )
        apply_font(self.find_clinics_button)  
        self.find_clinics_button.bind(on_press=self.find_nearby_clinics)
        layout.add_widget(self.find_clinics_button)

        
        self.back_button = Button(
            text="Back to Main Menu",
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

    def find_nearby_clinics(self, instance):
        latitude = 41.2995  
        longitude = 69.2401
        google_maps_url = f"https://www.google.com/maps/search/clinics/@{latitude},{longitude},15z"
        webbrowser.open(google_maps_url)

    def go_to_main_menu(self, instance):
        self.manager.current = "main_menu"
