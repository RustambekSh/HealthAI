from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from styles import apply_font
from languages import LANGUAGES 
from kivy.app import App
 
class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        layout = BoxLayout(orientation="vertical")

        
        with layout.canvas.before:
            Color(0.52, 0.66, 0.28, 1)  
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

        layout.bind(pos=self.update_rect, size=self.update_rect)

        
        self.app_name_label = Label(
            text="UzHealthAI",  
            font_size=48,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  
        )
        apply_font(self.app_name_label) 
        layout.add_widget(self.app_name_label)
        self.add_widget(layout)
        Clock.schedule_once(self.go_to_main_menu, 4)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        self.rect.size = instance.size

    def go_to_main_menu(self, dt):
        self.manager.current = "main_menu"
        self.dt = dt
        self.management = 10
        self.check_point = True

    def update_language(self):
        app = App.get_running_app()
        lang = app.current_language
        translations = LANGUAGES[lang]
        self.app_name_label.text = translations["app_name"]
