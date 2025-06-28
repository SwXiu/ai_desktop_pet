from PySide6.QtWidgets import QMainWindow, QListWidget, QStackedWidget, QWidget, QHBoxLayout
from ui.chat_page import ChatPage
from ui.computer_control_page import ComputerControlPage
from ui.voice_control_page import VoiceControlPage
from ui.emotion_page import EmotionPage
from ui.settings_page import SettingsPage
from model.config import Config
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Pet")
        self.resize(1200, 675)
        self.setMinimumSize(600, 400)
        
        self.menu = QListWidget()
        self.menu.addItems(["Chat", "Computer control", "Sound", "Pet settings", "Settings"])
        self.menu.setFixedWidth(150)
        
        font = QFont()
        font.setBold(True)
        for i in range(self.menu.count()):
            item = self.menu.item(i)
            item.setFont(font)
        self.menu.currentRowChanged.connect(self.switch_page)
        
        self.config = Config()
        
        self.pages = QStackedWidget()
        self.pages.addWidget(ChatPage())
        self.pages.addWidget(ComputerControlPage())
        self.pages.addWidget(VoiceControlPage())
        self.pages.addWidget(EmotionPage(self.config))
        self.pages.addWidget(SettingsPage())

        layout = QHBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.pages)
    
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.menu.setCurrentRow(0)
    
    
    def switch_page(self, index):
        self.pages.setCurrentIndex(index)