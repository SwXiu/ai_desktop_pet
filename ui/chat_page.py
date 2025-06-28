from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QLineEdit, QPushButton, QHBoxLayout
from model.chat_history import ChatHistory
from controller.app_manager import AppManager

class ChatPage(QWidget):
    def __init__(self, app_manager: AppManager):
        super().__init__()

        self.app_manager = app_manager
        self.history = self.app_manager.memory_manager.chat_history

        self.layout = QVBoxLayout(self)

        self.chat_display = QTextBrowser(self)
        self.layout.addWidget(self.chat_display)

        input_layout = QHBoxLayout()

        self.input_edit = QLineEdit(self)
        input_layout.addWidget(self.input_edit)

        self.send_button = QPushButton("发送", self)
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        self.layout.addLayout(input_layout)

        self.load_history()

    def load_history(self):
        for item in self.history.get_all():
            role = "你" if item["role"] == "user" else "AI"
            self.chat_display.append(f"<b>{role}：</b> {item['content']}")

    def send_message(self):
        user_text = self.input_edit.text().strip()
        if not user_text:
            return

        self.chat_display.append(f"<b>你：</b> {user_text}")
        self.history.append("user", user_text)

        reply = self.app_manager.chat(user_text)

        self.chat_display.append(f"<b>AI：</b> {reply}")
        self.history.append("assistant", reply)

        self.input_edit.clear()
