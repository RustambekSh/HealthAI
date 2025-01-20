from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from intro_screen import IntroScreen
from main_menu import MainMenuScreen
from symptom_checker import SymptomCheckerScreen
from clinic_finder import ClinicFinderScreen
from health_tips import HealthTipsScreen
from languages import LANGUAGES

class UzHealthAIApp(App):
    def build(self):
        # Create a screen manager with a fade transition
        self.screen_manager = ScreenManager(transition=FadeTransition())

        # Set the default language
        self.current_language = "en"

        # Add screens to the screen manager
        self.screen_manager.add_widget(IntroScreen(name="intro"))
        self.screen_manager.add_widget(MainMenuScreen(name="main_menu"))
        self.screen_manager.add_widget(SymptomCheckerScreen(name="symptom_checker"))
        self.screen_manager.add_widget(ClinicFinderScreen(name="clinic_finder"))
        self.screen_manager.add_widget(HealthTipsScreen(name="health_tips"))

        # Set the intro screen as the initial screen
        self.screen_manager.current = "intro"

        return self.screen_manager

    def switch_language(self, language_code):
        print(f"Switching to language: {language_code}")  # Debugging
        # Update the current language
        self.current_language = language_code

        # Refresh all screens to update the text
        for screen in self.screen_manager.screens:
            if hasattr(screen, "update_language"):
                print(f"Updating language for screen: {screen.name}")  # Debugging
                screen.update_language()


if __name__ == "__main__":
    UzHealthAIApp().run()