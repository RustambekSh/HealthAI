from kivy.uix.label import Label
from kivy.uix.button import Button

# Custom Font Path
FONT_PATH = "assets/Regular.ttf"

# Apply Times New Roman font to all labels and buttons
def apply_font(widget):
    if isinstance(widget, (Label, Button)):
        widget.font_name = FONT_PATH