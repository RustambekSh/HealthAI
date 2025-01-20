from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from styles import apply_font
import pyrebase
from languages import LANGUAGES

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Set background color
        with self.layout.canvas.before:
            Color(0.52, 0.66, 0.28, 1)  # Light green background
            self.rect = Rectangle(pos=self.layout.pos, size=self.layout.size)

        # Bind the rectangle size to the layout size
        self.layout.bind(pos=self.update_rect, size=self.update_rect)

        # Email Input
        self.email_input = TextInput(
            hint_text="Email",
            size_hint=(1, None),
            height=50,
            multiline=False
        )
        self.layout.add_widget(self.email_input)

        # Password Input
        self.password_input = TextInput(
            hint_text="Password",
            size_hint=(1, None),
            height=50,
            multiline=False,
            password=True
        )
        self.layout.add_widget(self.password_input)

        # Login Button
        self.login_button = Button(
            text="Login",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        apply_font(self.login_button)  # Apply custom font
        self.login_button.bind(on_press=self.login)
        self.layout.add_widget(self.login_button)

        # Signup Button
        self.signup_button = Button(
            text="Sign Up",
            size_hint=(None, None),
            size=(200, 50),
            background_color=(0.24, 0.48, 0.15, 1),  # Medium green
            color=(1, 1, 1, 1),  # White text
            bold=True
        )
        apply_font(self.signup_button)  # Apply custom font
        self.signup_button.bind(on_press=self.signup)
        self.layout.add_widget(self.signup_button)

        # Error Label
        self.error_label = Label(
            text="",
            font_size=14,
            bold=True,
            color=(1, 0, 0, 1)  # Red text for errors
        )
        apply_font(self.error_label)  # Apply custom font
        self.layout.add_widget(self.error_label)

        self.add_widget(self.layout)

    def update_rect(self, instance, value):
        # Update the rectangle size and position when the layout changes
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        try:
            # Sign in with Firebase
            user = auth.sign_in_with_email_and_password(email, password)
            self.manager.current = "main_menu"
        except Exception as e:
            self.error_label.text = str(e)

    def signup(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        try:
            # Create a new user with Firebase
            user = auth.create_user_with_email_and_password(email, password)
            self.manager.current = "main_menu"
        except Exception as e:
            self.error_label.text = str(e)

    def update_language(self):
        # Update the text based on the selected language
        app = App.get_running_app()
        lang = app.current_language
        translations = LANGUAGES[lang]

        self.email_input.hint_text = translations["email"]
        self.password_input.hint_text = translations["password"]
        self.login_button.text = translations["login"]
        self.signup_button.text = translations["signup"]