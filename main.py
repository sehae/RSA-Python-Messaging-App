import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from menu import Ui_MainWindow as MenuUI
from chat import ChatWindow

class MenuWindow(QMainWindow, MenuUI):
    def __init__(self):
        super(MenuWindow, self).__init__()
        self.setupUi(self)
        self.join_button.clicked.connect(self.open_chat)

    def open_chat(self):
        if len(ChatWindow.chat_windows) >= 2:
            QMessageBox.warning(self, "Sorry :(", "The room is already full.")
        else:
            screen_name = self.screen_name.text().strip()
            if screen_name:
                self.chat_window = ChatWindow(screen_name)
                self.chat_window.show()
                self.screen_name.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu_window = MenuWindow()
    menu_window.show()
    sys.exit(app.exec_())