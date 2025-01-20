from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from main_menu import MainMenuScreen
from symptom_checker import SymptomCheckerScreen
from clinic_finder import ClinicFinderScreen
from health_tips import HealthTipsScreen

class UzHealthAIApp(App):
    def build(self):
        # Create a screen manager
        self.screen_manager = ScreenManager()

        # Add screens to the screen manager
        self.screen_manager.add_widget(MainMenuScreen(name="main_menu"))
        self.screen_manager.add_widget(SymptomCheckerScreen(name="symptom_checker"))
        self.screen_manager.add_widget(ClinicFinderScreen(name="clinic_finder"))
        self.screen_manager.add_widget(HealthTipsScreen(name="health_tips"))

        return self.screen_manager

if __name__ == "__main__":
    UzHealthAIApp().run()