from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.mainwindow import Ui_MainWindow
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configure l'interface utilisateur

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Définir l'icône de la fenêtre
    icon_path = resource_path(os.path.join("resourses", "images", "logo.png"))
    if os.path.exists(icon_path):
        print(icon_path)
        app.setWindowIcon(QIcon(icon_path))
    else:
        print("Icon file not found")
    
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
