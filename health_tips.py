from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout 
from kivy.graphics import Color, Rectangle
from styles import apply_font

class HealthTipsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)    
        with layout.canvas.before:
            Color(0.52, 0.66, 0.28, 1)  
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

       
        layout.bind(pos=self.update_rect, size=self.update_rect)
        self.tips_label = Label(
            text="1. Drink plenty of water.\n2. Wash your hands regularly.\n3. Get enough sleep. \n4. Take care of yourself everyday!",
            font_size=14,
            bold=True,
            color=(0.07, 0.21, 0.14, 1)  
        )
        apply_font(self.tips_label)  
        layout.add_widget(self.tips_label)

        
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

    def go_to_main_menu(self, instance):
        self.manager.current = "main_menu"
