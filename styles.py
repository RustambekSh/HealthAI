from kivy.uix.label import Label
from kivy.uix.button import Button

FONT_PATH = "assets\PlaywriteVN-Regular.ttf"

def apply_font(widget):
    if isinstance(widget, (Label, Button)):
        widget.font_name = FONT_PATH
