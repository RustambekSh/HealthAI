from toga.style import Pack

# Color Scheme
COLOR_BACKGROUND = "#85A947"  # Light green
COLOR_BUTTON = "#3E7B27"      # Medium green
COLOR_TEXT = "#123524"        # Dark green
COLOR_FOOTER_BACKGROUND = "#3E7B27"  # Medium green for footer

# General Styles
def create_button_style():
    return Pack(
        background_color=COLOR_BUTTON,
        padding=20,  # Increased padding for bigger buttons
        color=COLOR_TEXT,
        font_weight="bold",
        width=200,  # Fixed width for buttons
        text_align="center",
    )

def create_label_style():
    return Pack(
        color=COLOR_TEXT,
        font_weight="bold"
    )

def create_box_style():
    return Pack(
        direction="column",
        padding=20,
        background_color=COLOR_BACKGROUND
    )

def create_header_style():
    return Pack(
        color=COLOR_TEXT,
        font_size=24,
        font_weight="bold",
        padding_bottom=20,
        text_align="center"
    )

def create_footer_style():
    return Pack(
        background_color=COLOR_FOOTER_BACKGROUND,
        padding=10,
        color=COLOR_TEXT,
        font_weight="bold",
        text_align="center"
    )