"""
Desining an application with more features for libre
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class LibrePlus(toga.App):

    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_label = toga.Label(
            "Welcome to LibrePlus",
            style=Pack(padding=(0, 5))
        )
        self_email_input = toga.TextInput(
            placeholder="Your email",
            style=Pack(padding=5, flex=1)
        )
        self_password_input = toga.TextInput(
            placeholder="Your password",
            style=Pack(padding=5, flex=1)
        )
        login_button = toga.Button(
            "Login",
            style=Pack(padding=5)
        )
        main_box.add(main_label)
        main_box.add(self_email_input)
        main_box.add(self_password_input)
        main_box.add(login_button)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return LibrePlus()
