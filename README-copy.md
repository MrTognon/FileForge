# FileForge
  Application permettant de modifier le nom de fichier des détecteurs BATmode S+ pour les adapter au format du détecteur SM4BAT.

# Technologies utilises
  Cette application est code en python et utilise la bibliotheque PyQt5 pour gerer l'affichage des fenetres. L'application Qt Designer et egalement utilise pour faciliter le developpement de l'interface.

# Commandes importantes pour le developpement du projet
- `python main.py` — Va lancer l'application en mode developpement
- `pyinstaller --noconfirm --onefile --windowed --icon "F:/Projets persos/FileForge/resources/icons/logo.ico" --name "FileForge" --add-data "F:/Projets persos/FileForge/resources/icons;resources/icons" main.py` — Va lancer la compilation de l'application

# Commandes pour installer les bibliothques necessaires
- `python -m pip install virtualenv` — Installation de virtualenv
- `virtualenv venv_pyqt` — Permet de creer un environnement virtuel pour installer les dependances
- `pip install pyqt5` — Installation de pyqt5
- `pyuic5 -x ui/mainwindow.ui -o ui/mainwindow.py` — Permet de convertir une interface .ui en .py
- `pip install pyinstaller` — Installation du compilateur python