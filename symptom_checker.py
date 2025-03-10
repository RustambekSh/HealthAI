from kivy.uix.screenmanager import Screen 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from styles import apply_font
from languages import LANGUAGES
from kivy.app import App
import google.generativeai as genai

class ChatBubble(Label):
    def __init__(self, text, is_user=False, **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.size_hint = (None, None)
        self.size = (self.texture_size[0] + 20, self.texture_size[1] + 20)
        self.padding = (10, 10)
        self.halign = 'right' if is_user else 'left'
        self.valign = 'center'
        self.color = (0.07, 0.21, 0.14, 1) if is_user else (0.3, 0.3, 0.3, 1)
        self.bold = True
        self.font_size = 14
        
        with self.canvas.before:
            Color(rgba=(0.85, 0.9, 0.8, 1) if is_user else (1, 1, 1, 1))
            self.rect = Rectangle(pos=self.pos, size=self.size)
            
        self.bind(size=self._update_rect, pos=self._update_rect)
        
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class SymptomCheckerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chat_history = []
        self.setup_ui()
        genai.configure(api_key='') # Put your APi key here
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.thinking = False

    def setup_ui(self):
        main_layout = BoxLayout(orientation='vertical', spacing=25)
        
        # Header
        header = BoxLayout(size_hint=(1, None), height=50)
        with header.canvas.before:
            Color(0.24, 0.48, 0.15, 1)
            Rectangle(pos=header.pos, size=header.size)
        self.header_label = Label(text="Health Assistant", color=(1,1,1,1), bold=True)
        apply_font(self.header_label)
        header.add_widget(self.header_label)
        main_layout.add_widget(header)
        
        # Chat History
        self.chat_scroll = ScrollView()
        self.chat_layout = BoxLayout(
            orientation='vertical', 
            spacing=10, 
            size_hint_y=None,
            padding=(20, 10)
        )
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.chat_scroll.add_widget(self.chat_layout)
        main_layout.add_widget(self.chat_scroll)
        
        # Input Area
        input_box = BoxLayout(size_hint=(1, None), height=60, spacing=10, padding=(10, 5))
        self.input_field = TextInput(
            hint_text="Type your symptoms here...",
            multiline=True,
            background_color=(1, 1, 1, 1),
            foreground_color=(0.07, 0.21, 0.14, 1),
            size_hint=(0.8, 1))
        self.input_field.bind(on_text_validate=self.send_message)
        
        self.send_btn = Button(
            text="Send",
            size_hint=(0.2, 1),
            background_color=(0.24, 0.48, 0.15, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        apply_font(self.send_btn)
        self.send_btn.bind(on_press=self.send_message)
        
        input_box.add_widget(self.input_field)
        input_box.add_widget(self.send_btn)
        main_layout.add_widget(input_box)
        
        self.add_widget(main_layout)

    def add_message(self, text, is_user=False):
        bubble = ChatBubble(text, is_user=is_user)
        self.chat_layout.add_widget(bubble)
        Clock.schedule_once(lambda dt: self.chat_scroll.scroll_to(bubble), 0.1)

    def send_message(self, instance):
        if self.thinking:
            return
            
        user_input = self.input_field.text.strip()
        if not user_input:
            return
            
        self.add_message(user_input, is_user=True)
        self.input_field.text = ''
        self.thinking = True
        self.add_message("Thinking...", is_user=False)
        
        Clock.schedule_once(lambda dt: self.generate_response(user_input), 0.1)

    def generate_response(self, user_input):
        try:
            response = self.model.generate_content(
                f"Act as a medical assistant. The user says: {user_input}. "
                "Provide a helpful response with possible causes and suggestions. "
                "Keep it under 150 words and use simple language."
            )
            self.chat_layout.remove_widget(self.chat_layout.children[0])  # Remove "Thinking..."
            self.add_message(response.text, is_user=False)
        except Exception as e:
            self.add_message(f"Error: {str(e)}", is_user=False)
        finally:
            self.thinking = False

    def update_language(self):
        app = App.get_running_app()
        lang = app.current_language
        translations = LANGUAGES[lang]
        
        self.header_label.text = translations["health_assistant"]
        self.input_field.hint_text = translations["type_symptoms"]
        self.send_btn.text = translations["send"]
        
        for child in self.chat_layout.children:
            if isinstance(child, ChatBubble) and child.text == "Thinking...":
                child.text = translations["thinking"]

    def on_enter(self):
        self.chat_layout.clear_widgets()
        self.input_field.text = ''
        self.thinking = False
