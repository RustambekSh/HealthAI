from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from styles import apply_font
from languages import LANGUAGES
from kivy.app import App

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

       
        with self.layout.canvas.before:
            Color(0.52, 0.66, 0.28, 1)  
            self.rect = Rectangle(pos=self.layout.pos, size=self.layout.size)

        self.layout.bind(pos=self.update_rect, size=self.update_rect)

        self.header_label = Label(
            text="UzHealthAI",
            font_size=24,
            bold=True,
            color=(0.07, 0.21, 0.14, 1) 
        )
        apply_font(self.header_label)  
        self.layout.add_widget(self.header_label)

        self.language_button = Button(
            text="Language",
            size_hint=(None, None),
            size=(100, 50),
            background_color=(0.24, 0.48, 0.15, 1), 
            color=(1, 1, 1, 1),  
            bold=True
        )
        apply_font(self.language_button) 
        self.language_button.bind(on_release=self.show_language_dropdown)
        self.layout.add_widget(self.language_button)

        self.button_box = BoxLayout(orientation="vertical", size_hint=(None, None), size=(200, 200), spacing=20)
        self.button_box.pos_hint = {"center_x": 0.5, "center_y": 0.5}  

        self.ai_button = Button(
            text="AI Symptom Checker",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1), 
            color=(1, 1, 1, 1),  
            bold=True
        )
        apply_font(self.ai_button) 
        self.ai_button.bind(on_press=self.go_to_symptom_checker)
        self.button_box.add_widget(self.ai_button)

        self.clinic_button = Button(
            text="Find Clinics",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1), 
            color=(1, 1, 1, 1),  
            bold=True
        )
        apply_font(self.clinic_button)  
        self.clinic_button.bind(on_press=self.go_to_clinic_finder)
        self.button_box.add_widget(self.clinic_button)

        self.tips_button = Button(
            text="Health Tips",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1), 
            color=(1, 1, 1, 1),  
            bold=True
        )
        apply_font(self.tips_button)  
        self.tips_button.bind(on_press=self.go_to_health_tips)
        self.button_box.add_widget(self.tips_button)

        self.layout.add_widget(self.button_box)

        self.add_widget(self.layout)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def show_language_dropdown(self, instance):
        dropdown = DropDown()

     
        for lang_code, lang_data in LANGUAGES.items():
            btn = Button(
                text=lang_data["language_name"], 
                size_hint_y=None,
                height=50,
                background_color=(0.24, 0.48, 0.15, 1),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_release=lambda btn, lc=lang_code: self.switch_language(lc))
            dropdown.add_widget(btn)

        dropdown.open(instance)

    def switch_language(self, lang_code):
        print(f"Switching to language code: {lang_code}")
        app = App.get_running_app()
        app.switch_language(lang_code)

    def go_to_symptom_checker(self, instance):
        self.manager.current = "symptom_checker"

    def go_to_clinic_finder(self, instance):
        self.manager.current = "clinic_finder"

    def go_to_health_tips(self, instance):
        self.manager.current = "health_tips"

    def update_language(self):
        app = App.get_running_app()
        lang = app.current_language
        translations = LANGUAGES[lang]
        print(f"Updating MainMenuScreen with language: {lang}") 
        self.ai_button.text = translations["ai_symptom_checker"]
        self.clinic_button.text = translations["find_clinics"]
        self.tips_button.text = translations["health_tips"]
        self.header_label.text = translations["app_name"]

        self.ai_button.canvas.ask_update()
        self.clinic_button.canvas.ask_update()
        self.tips_button.canvas.ask_update()
        self.header_label.canvas.ask_update()
