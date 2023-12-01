from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.mainwindow import Ui_MainWindow
import os

class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configure l'interface utilisateur

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Définir l'icône de la fenêtre
    icon_path = os.path.join("resources", "images", "logo.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
