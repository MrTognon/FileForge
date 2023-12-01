from PyQt5 import QtWidgets
from ui.mainwindow import Ui_MainWindow  # Assurez-vous que le chemin d'importation est correct

class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configure l'interface utilisateur
        # Ajoutez ici la logique supplémentaire de votre application

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
