from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QLineEdit, QPushButton, QHBoxLayout

class ChatPage(QWidget):
    def __init__(self):
        super().__init__()

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

    def send_message(self):
        user_text = self.input_edit.text().strip()
        if user_text:
            self.chat_display.append(f"<b>你：</b> {user_text}")

            self.chat_display.append(f"<b>AI：</b> 我收到了你的消息：{user_text}")

            self.input_edit.clear()