from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.mainwindow import Ui_MainWindow
import os, sys

#* Fonction pour obtenir le chemin absolu d'un fichier
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        #* PyInstaller crée un dossier temporaire et utilise ce chemin pour les ressources
        base_path = sys._MEIPASS
    except Exception:
        #* Si l'application est exécutée en mode développement, utilise le chemin courant
        base_path = os.path.abspath(".")
    #* Retourne le chemin absolu du fichier
    return os.path.join(base_path, relative_path)

#* Classe de la fenêtre principale
class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  #* Configure l'interface utilisateur

#* Fonction principale
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #* Définir l'icône de la fenêtre
    icon_path = resource_path(os.path.join("resources", "icons", "logo.ico"))
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
