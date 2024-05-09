from PyQt5 import QtCore, QtGui, QtWidgets
from logwindow import LogWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 350))
        MainWindow.setMaximumSize(QtCore.QSize(350, 350))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #c9184a;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(35)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("QLabel {\n"
"    color: #ffb3c1;\n"
"}\n"
"")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.screen_name = QtWidgets.QLineEdit(self.centralwidget)
        self.screen_name.setMinimumSize(QtCore.QSize(0, 50))
        self.screen_name.setClearButtonEnabled(True)
        self.screen_name.setObjectName("screen_name")
        self.verticalLayout.addWidget(self.screen_name)
        self.join_button = QtWidgets.QPushButton(self.centralwidget)
        self.join_button.setMinimumSize(QtCore.QSize(0, 35))
        self.join_button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.join_button.setFont(font)
        self.join_button.setStyleSheet("QPushButton {\n"
"    background-color: #ff758f;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ff6080;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ff506f; \n"
"}\n"
"")
        self.join_button.setObjectName("join_button")
        self.verticalLayout.addWidget(self.join_button)

        # Add a new button to open the password window
        self.password_button = QtWidgets.QPushButton(self.centralwidget)
        self.password_button.clicked.connect(self.open_password_window)
        self.verticalLayout.addWidget(self.password_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PairPal"))
        self.title_label.setText(_translate("MainWindow", "PairPal"))
        self.screen_name.setPlaceholderText(_translate("MainWindow", "Enter your Screen Name"))
        self.join_button.setText(_translate("MainWindow", "Join"))
        self.password_button.setText(_translate("MainWindow", "Open Log Window"))

    def open_password_window(self):
        self.password_window = QtWidgets.QWidget()
        self.password_window.setWindowTitle("Enter Password")

        self.password_field = QtWidgets.QLineEdit(self.password_window)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)

        self.log_button = QtWidgets.QPushButton("Open", self.password_window)
        self.log_button.clicked.connect(self.check_password)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.password_field)
        layout.addWidget(self.log_button)
        self.password_window.setLayout(layout)

        self.password_window.show()

    def check_password(self):
        if self.password_field.text() == "admin123":
            self.log_window = LogWindow()
            self.log_window.show()
            self.password_window.close()
        else:
            QtWidgets.QMessageBox.warning(self.password_window, "Error", "Incorrect password.")
