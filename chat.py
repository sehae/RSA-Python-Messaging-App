from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode
from logwindow import LogWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #c9184a;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("QLabel {\n"
"    color: #ffb3c1;\n"
"}\n"
"")
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.chat_history = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chat_history.setFont(font)
        self.chat_history.setStyleSheet("QTextEdit {\n"
"    background-color: #ffccd5;\n"
"    border: 1px solid #ff4d6d;\n"
"}\n"
"")
        self.chat_history.setReadOnly(True)
        self.chat_history.setObjectName("chat_history")
        self.verticalLayout.addWidget(self.chat_history)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.send_button = QtWidgets.QTextEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)
        self.send_button.setMinimumSize(QtCore.QSize(0, 60))
        self.send_button.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("QTextEdit {\n"
"    background-color: #ffccd5;\n"
"    border: 1px solid #ff4d6d;\n"
"}\n"
"")
        self.send_button.setObjectName("send_button")
        self.horizontalLayout.addWidget(self.send_button)
        self.message_input = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_input.sizePolicy().hasHeightForWidth())
        self.message_input.setSizePolicy(sizePolicy)
        self.message_input.setMinimumSize(QtCore.QSize(100, 35))
        self.message_input.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.message_input.setFont(font)
        self.message_input.setStyleSheet("QPushButton {\n"
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
        self.message_input.setObjectName("message_input")
        self.message_input.clicked.connect(self.send_message)
        self.horizontalLayout.addWidget(self.message_input)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome!"))
        self.title_label.setText(_translate("MainWindow", "PairPal"))
        self.chat_history.setPlaceholderText(_translate("MainWindow", "There\'s nothing here..."))
        self.send_button.setPlaceholderText(_translate("MainWindow", "Write a message..."))
        self.message_input.setText(_translate("MainWindow", "Send"))

class ChatWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    chat_windows = []

    def __init__(self, screen_name, log_window):
        super(ChatWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Welcome {screen_name} to PairPal")
        self.screen_name = screen_name
        self.chat_windows.append(self)
        self.log_window = log_window

        self.key_pair = RSA.generate(2048)
        self.public_key = self.key_pair.publickey()

        if self.log_window is not None:
            self.log_window.append_log(f"[{self.screen_name}] Key pair generated.", '#FFFFFF')

    def send_message(self):
        message = self.send_button.toPlainText()
        if message:
            encrypted_messages = self.encrypt_message(message)
            if self.log_window is not None:
                self.log_window.append_log(f"[{self.screen_name}] SENT Encrypted messages: {encrypted_messages}", '#FF0000')

            self.append_to_chat_history(f"You: {message}")

            if self.log_window is not None:
                self.log_window.append_log(f"[{self.screen_name}] Sent message: {message}", '#FFFFFF')

            for window in self.chat_windows:
                if window != self:
                    window.receive_message(self.screen_name, self.public_key, encrypted_messages)

            self.send_button.clear()

    def receive_message(self, sender_screen_name, sender_public_key, encrypted_messages):
        if self.log_window is not None:
            self.log_window.append_log(f"[{sender_screen_name}] RECEIVED Encrypted messages: {encrypted_messages}", '#FF0000')
        decrypted_messages = self.decrypt_message(encrypted_messages)
        for decrypted_message in decrypted_messages:
            if self.log_window is not None:
                self.log_window.append_log(f"[{sender_screen_name}] Decrypted message: '{decrypted_message}'", '#00FF00')
            if decrypted_message and decrypted_message != 'You':
                self.append_to_chat_history(f"{sender_screen_name}: {decrypted_message}")

    def encrypt_message(self, message):
        encrypted_messages = []
        for window in self.chat_windows:
            if window != self:
                cipher_rsa = PKCS1_OAEP.new(window.public_key)
                encrypted_data = cipher_rsa.encrypt(message.encode())
                encrypted_messages.append(b64encode(encrypted_data).decode())
        return encrypted_messages

    def decrypt_message(self, encrypted_messages):
        decrypted_messages = []
        for encrypted_message in encrypted_messages:
            encrypted_data = b64decode(encrypted_message.encode())
            cipher_rsa = PKCS1_OAEP.new(self.key_pair)
            decrypted_data = cipher_rsa.decrypt(encrypted_data)
            decrypted_messages.append(decrypted_data.decode())
        return decrypted_messages

    def append_to_chat_history(self, message):
        self.chat_history.append(message)

    def closeEvent(self, event):
        self.chat_windows.remove(self)
        event.accept()

    @classmethod
    def close_all(cls):
        for window in cls.chat_windows:
            window.close()