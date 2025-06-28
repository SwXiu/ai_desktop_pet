from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QSlider, QMessageBox
from PySide6.QtCore import Qt

class EmotionPage(QWidget):
    def __init__(self, config, live2d_controller=None):
        super().__init__()
        self.config = config
        self.live2d_controller = live2d_controller

        self.layout = QVBoxLayout(self)

        self.name_label = QLabel("用户名")
        self.name_edit = QLineEdit(self.config.user_name)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_edit)

        self.prompt_label = QLabel("桌宠性格 Prompt：")
        self.prompt_edit = QTextEdit()
        self.prompt_edit.setPlainText(self.config.personality_prompt)
        self.layout.addWidget(self.prompt_label)
        self.layout.addWidget(self.prompt_edit)

        self.temp_label = QLabel(f"Temperature: {self.config.temperature:.2f}")
        self.layout.addWidget(self.temp_label)

        self.temp_slider = QSlider(Qt.Horizontal)
        self.temp_slider.setMinimum(0)
        self.temp_slider.setMaximum(100)
        self.temp_slider.setValue(int(self.config.temperature * 100))
        self.temp_slider.valueChanged.connect(self.on_temp_changed)
        self.layout.addWidget(self.temp_slider)

        save_btn = QPushButton("保存设置")
        save_btn.clicked.connect(self.save_settings)
        self.layout.addWidget(save_btn)

        if self.live2d_controller:
            self.expression_label = QLabel("当前表情: None")
            self.layout.addWidget(self.expression_label)

    def on_temp_changed(self, value):
        temp = value / 100
        self.temp_label.setText(f"Temperature: {temp:.2f}")
        self.config.temperature = temp

    def save_settings(self):
        self.config.user_name = self.name_edit.text()
        self.config.personality_prompt = self.prompt_edit.toPlainText()
        self.config.save()
        QMessageBox.information(self, "提示", "设置已保存")

    def update_expression(self, expression_name):
        if hasattr(self, 'expression_label'):
            self.expression_label.setText(f"当前表情: {expression_name}")
