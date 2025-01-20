import toga
from styles import create_button_style, create_label_style, create_box_style
import webbrowser

class ClinicFinder:
    def __init__(self, main_window, on_back_click):
        self.main_window = main_window
        self.on_back_click = on_back_click

        # UI Elements
        self.map_label = toga.Label(
            "Click the button below to find nearby clinics.",
            style=create_label_style()
        )
        self.find_clinics_button = toga.Button(
            "Find Clinics",
            on_press=self.find_nearby_clinics,
            style=create_button_style()
        )
        self.back_button = toga.Button(
            "Back to Main Menu",
            on_press=self.on_back_click,
            style=create_button_style()
        )

        # Layout
        self.box = toga.Box(
            children=[self.map_label, self.find_clinics_button, self.back_button],
            style=create_box_style()
        )

    def find_nearby_clinics(self, widget):
        try:
            location = self.get_user_location()
            if location:
                latitude, longitude = location
                self.open_google_maps(latitude, longitude)
            else:
                self.map_label.text = "Unable to retrieve your location. Please enable location services."
        except Exception as e:
            self.map_label.text = f"Error: {str(e)}"

    def get_user_location(self):
        # For demonstration, we'll use a hardcoded location (Tashkent, Uzbekistan)
        latitude = 41.2995
        longitude = 69.2401
        return latitude, longitude

    def open_google_maps(self, latitude, longitude):
        google_maps_url = f"https://www.google.com/maps/search/clinics/@{latitude},{longitude},15z"
        webbrowser.open(google_maps_url)