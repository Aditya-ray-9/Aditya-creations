from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass

class CalculatorApp(App):
    def build(self):
        self.icon = 'calculator_icon.PNG'  # Optional: add your own icon
        self.title = "Calculator"
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        self.display = TextInput(multiline=True, readonly=True, halign="right", font_size=32, size_hint=(1, 0.2))
        main_layout.add_widget(self.display)

        button_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.8))

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+'
        ]

        for button in buttons:
            button_layout.add_widget(Button(text=button, pos_hint={"center_x": 0.5, "center_y": 0.5}, 
                                            on_press=self.on_button_press, 
                                            background_color=(0, 0, 0, 1), 
                                            color=(1, 1, 1, 1)))

        button_layout.add_widget(Button(text='=', pos_hint={"center_x": 0.5, "center_y": 0.5}, 
                                        on_press=self.on_solution, 
                                        background_color=(0, 0, 0, 1), 
                                        color=(1, 1, 1, 1)))

        main_layout.add_widget(button_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text

        if button_text == 'C':
            self.display.text = ''
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.display.text = new_text

        self.last_was_operator = button_text in self.operators
        self.last_button = button_text

    def on_solution(self, instance):
        text = self.display.text
        if text:
            if text == '1122':
                self.show_app_controls()
            else:
                try:
                    solution = str(eval(self.display.text))
                    self.display.text += f"\n= {solution}"
                except Exception as e:
                    self.display.text += "\nError"

    def show_app_controls(self):
        layout = BoxLayout(orientation='vertical')
        add_button = Button(text='Add App')
        exit_button = Button(text='Exit')
        layout.add_widget(add_button)

        layout.add_widget(exit_button)

        popup = Popup(title='App Controls', content=layout, size_hint=(None, None), size=(200, 100))
        add_button.bind(on_press=self.show_installed_apps)
        exit_button.bind(on_press=popup.dismiss)
        popup.open()

    def show_installed_apps(self, instance):
        popup = Popup(title='Installed Apps', size_hint=(None, None), size=(300, 300))
        layout = GridLayout(cols=2, spacing=5)
        if platform == 'android':
            activity = autoclass('org.kivy.android.PythonActivity').mActivity
            package_manager = activity.getPackageManager()
            packages = package_manager.getPackagesHoldingPermissions(["android.permission.INTERNET"], 0)
            if packages:
                for package in packages:
                    app_name = package.applicationInfo.loadLabel(package_manager)
                    button = Button(text=app_name, size_hint=(None, None), size=(150, 50))
                    toggle_button = Button(text='+', size_hint=(None, None), size=(50, 50))
                    toggle_button.bind(on_press=self.toggle_app_visibility)
                    layout.add_widget(button)
                    layout.add_widget(toggle_button)
            else:
                print("No installed apps found.")

        popup.content = layout
        popup.open()

    def toggle_app_visibility(self, instance):
        if instance.text == '+':
            instance.text = '-'
            instance.background_color = (1, 0, 0, 1)  # Change to red
        else:
            instance.text = '+'
            instance.background_color = (0, 1, 0, 1)  # Change to green

if __name__ == '__main__':
    Window.size = (360, 640)  # Common phone resolution
    CalculatorApp().run()
