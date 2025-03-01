import toga
from main_menu import MainMenu
from symptom_checker import SymptomChecker
from clinic_finder import ClinicFinder
from health_tips import HealthTips


class UzHealthApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title="UzHealth AI", size=(400, 600))
        self.show_main_menu()

    def show_main_menu(self):
        self.main_menu = MainMenu(
            self.main_window,
            on_ai_click=self.show_ai_screen,
            on_clinic_click=self.show_clinic_screen,
            on_tips_click=self.show_tips_screen
        ) 
        self.main_window.content = self.main_menu.box
        self.main_window.show()

    def show_ai_screen(self, widget):
        self.symptom_checker = SymptomChecker(self.main_window, on_back_click=self.show_main_menu)
        self.main_window.content = self.symptom_checker.box

    def show_clinic_screen(self, widget):
        self.clinic_finder = ClinicFinder(self.main_window, on_back_click=self.show_main_menu)
        self.main_window.content = self.clinic_finder.box

    def show_tips_screen(self, widget):
        self.health_tips = HealthTips(self.main_window, on_back_click=self.show_main_menu)
        self.main_window.content = self.health_tips.box
