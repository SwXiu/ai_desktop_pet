import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from controller.app_manager import AppManager
from model.config import Config
from PySide6.QtGui import QIcon
import qt_material

def main():
    try:
        config = Config()
        app_manager = AppManager(config)

        app = QApplication(sys.argv)

        qt_material.apply_stylesheet(app, theme='sakura.xml')
        app.setStyleSheet(app.styleSheet() + load_qss('styles/sakura.qss'))

        window = MainWindow(app_manager)
        window.setWindowIcon(QIcon('assets/icon.png'))
        window.show()

        print(f"程序启动，当前使用AI模型: {config.default_ai_name}")
        sys.exit(app.exec())
    except Exception as e:
        print("程序异常退出:", e)
        
def load_qss(path):
    with open(path, encoding='utf-8') as f:
        return f.read()
    
if __name__ == "__main__":
    main()