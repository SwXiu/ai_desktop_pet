from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QHBoxLayout

class ComputerControlPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Computer Control")
        self.setFixedSize(1200, 675)
        
        layout = QVBoxLayout(self)
        
        self.control_display = QTextEdit()
        self.control_display.setReadOnly(True)
        layout.addWidget(self.control_display)
        
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your command here...")
        input_layout.addWidget(self.input_field)
        
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_command)
        input_layout.addWidget(send_button)
        
        layout.addLayout(input_layout)

    def send_command(self):
        command_text = self.input_field.text()
        if command_text:
            self.control_display.append(f"Command: {command_text}")
            self.input_field.clear()