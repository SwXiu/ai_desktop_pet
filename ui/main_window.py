from PySide6.QtWidgets import QMainWindow, QListWidget, QStackedWidget, QWidget, QHBoxLayout
from ui.chat_page import ChatPage
from ui.computer_control_page import ComputerControlPage
from ui.voice_control_page import VoiceControlPage
from ui.emotion_page import EmotionPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Pet")
        self.setFixedSize(1200, 675)
        
        self.menu = QListWidget()
        self.menu.addItems(["Chat", "Computer control", "Sound", "Pet settings"])
        self.menu.setFixedWidth(120)
        self.menu.currentRowChanged.connect(self.switch_page)
        
        self.pages = QStackedWidget()
        self.pages.addWidget(ChatPage())
        self.pages.addWidget(ComputerControlPage())
        self.pages.addWidget(VoiceControlPage())
        self.pages.addWidget(EmotionPage())

        layout = QHBoxLayout()
        layout.addWidget(self.menu)
        layout.addWidget(self.pages)
    
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.menu.setCurrentRow(0)
    
    
    def switch_page(self, index):
        self.pages.setCurrentIndex(index)