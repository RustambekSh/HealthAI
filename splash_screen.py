from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from styles import apply_font

class SplashScreen(Screen):
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

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
