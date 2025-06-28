from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QHBoxLayout

class EmotionPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pet Settings")
        self.setFixedSize(1200, 675)
        
        layout = QVBoxLayout(self)
        
        self.emotion_display = QTextEdit()
        self.emotion_display.setReadOnly(True)
        layout.addWidget(self.emotion_display)
        
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your emotion here...")
        input_layout.addWidget(self.input_field)
        
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_emotion)
        input_layout.addWidget(send_button)
        
        layout.addLayout(input_layout)

    def send_emotion(self):
        emotion_text = self.input_field.text()
        if emotion_text:
            self.emotion_display.append(f"Emotion: {emotion_text}")
            self.input_field.clear()