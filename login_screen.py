from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from styles import apply_font
from languages import LANGUAGES 


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        with self.layout.canvas.before:
            Color(0.52, 0.66, 0.28, 1)  
            self.rect = Rectangle(pos=self.layout.pos, size=self.layout.size)

        
        self.layout.bind(pos=self.update_rect, size=self.update_rect)
        self.email_input = TextInput(
            hint_text="Email",
            size_hint=(1, None),
            height=50,
            multiline=False
        )
        self.layout.add_widget(self.email_input)
        self.password_input = TextInput(
            hint_text="Password",
            size_hint=(1, None),
            height=50,
            multiline=False,
            password=True
        )
        self.layout.add_widget(self.password_input)
        self.login_button = Button(
            text="Login",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),  
            color=(1, 1, 1, 1),  
            bold=True
        )
        apply_font(self.login_button)  
        self.login_button.bind(on_press=self.login)
        self.layout.add_widget(self.login_button)

        
        self.signup_button = Button(
            text="Sign Up",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),  
            color=(1, 1, 1, 1),  
            bold=True
        )
        apply_font(self.signup_button)  
        self.signup_button.bind(on_press=self.signup)
        self.layout.add_widget(self.signup_button)
        
        self.error_label = Label(
            text="",
            font_size=14,
            bold=True,
            color=(1, 0, 0, 1)  
        )
        apply_font(self.error_label)  
        self.layout.add_widget(self.error_label)

        self.add_widget(self.layout)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


    #I have deleted login and sign in sections.
    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            self.manager.current = "main_menu"
        except Exception as e:
            self.error_label.text = str(e)

    def signup(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        try:
            user = auth.create_user_with_email_and_password(email, password)
            self.manager.current = "main_menu"
        except Exception as e:
            self.error_label.text = str(e)
    #Language is getting updated here.
    def update_language(self):
        app = App.get_running_app()
        lang = app.current_language
        translations = LANGUAGES[lang]
        self.email_input.hint_text = translations["email"]
        self.password_input.hint_text = translations["password"]
        self.login_button.text = translations["login"]
        self.signup_button.text = translations["signup"]
