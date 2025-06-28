from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox

class SettingsPage(QWidget):
    def __init__(self, app_manager):
        super().__init__()
        self.app_manager = app_manager

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Select AI："))

        self.ai_selector = QComboBox()
        self.ai_selector.addItems(["GPT", "DeepSeek"])
        self.ai_selector.currentTextChanged.connect(self.on_ai_changed)
        layout.addWidget(self.ai_selector)

    def on_ai_changed(self, ai_name):
        self.app_manager.switch_ai_client(ai_name)