from PyQt5 import QtWidgets, QtGui

class LogWindow(QtWidgets.QWidget):
    def __init__(self):
        super(LogWindow, self).__init__()
        self.setWindowTitle("System Logs")
        self.setStyleSheet("background-color: #333333; color: #CCCCCC;")
        self.log_text = QtWidgets.QTextEdit(self)
        self.log_text.setReadOnly(True)
        self.clear_button = QtWidgets.QPushButton("Clear", self)
        self.clear_button.setStyleSheet("background-color: #FFFFFF; color: #000000;")
        self.clear_button.clicked.connect(self.clear_logs)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.log_text)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

    def append_log(self, log, color):
        formatted_log = f"<font color='{color}'>{log}</font>"
        self.log_text.insertHtml(formatted_log + "<br>")
        self.log_text.moveCursor(QtGui.QTextCursor.End)


    def clear_logs(self):
        self.log_text.clear()