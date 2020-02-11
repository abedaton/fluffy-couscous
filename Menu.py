from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
                            QPushButton, QSlider,QHBoxLayout,QVBoxLayout,QTabWidget,QSpinBox, QLabel,\
                            QDoubleSpinBox,QComboBox

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
import sys

from GUI_pyqt import *
from PyQt5.QtGui import QBrush, QPixmap, QPalette, QImage



class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.setBackground(QImage("Images/biohazard.jpg"), self.width(), self.height())
        self.combo = QComboBox(self)
        self.combo.addItem("SIR")
        self.combo.addItem("SEIHFR")
        self.combo.addItem("SEIHFBR")
        self.combo.addItem("SEIRS")
        self.combo.addItem("Dispersion spatiale")
        self.combo.addItem("Effet du vaccin")
        self.combo.addItem("Map")

        self.comboMap = QComboBox(self)
        self.comboMap.addItem("PlateCarree")
        self.comboMap.addItem("Miller")
        self.comboMap.addItem("Mollweide")
        self.comboMap.addItem("EckertIII")
        self.comboMap.addItem("EuroPP")
        self.comboMap.hide()

        self.combo.currentIndexChanged.connect(lambda: self.showNewCombo() if self.combo.currentIndex() == 6 else self.comboMap.hide() if not self.comboMap.isHidden() else None)


        self.button = QPushButton("GO",self)
        self.button.clicked.connect(self.choose_model)
        self.button.keyPressEvent = self.keyPressEvent

        
        self.hbox = QHBoxLayout()
        #hbox.addStretch(1)
        self.hbox.addWidget(self.button)
        self.hbox.addWidget(self.combo)
        self.hbox.setAlignment(Qt.AlignCenter)
        
        
        #vbox = QVBoxLayout(self)
        #vbox.addStretch(1)
        #vbox.addWidget(self.button2)
        
        #vbox.addLayout(hbox)
        self.setLayout(self.hbox)
        
        self.showMaximized()

    def setBackground(self, aimage, width = None, height = None):
        image = aimage.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        sImage = image.scaled(QSize(width, height))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)


    def keyPressEvent(self, e):
        if e.key() == 16777220:
            print("hey")
            self.choose_model()


    def choose_model(self):
        from GUI_pyqt import App

        model_name = self.combo.currentText()
        if (model_name == "SIR"):
            from GUI_pyqt import SIR
            self.app2 = App(SIR())
        elif (model_name == "SEIRS"):
            from GUI_pyqt import SEIRS
            self.app2 = App(SEIRS())
        elif (model_name == "SEIHFR"):
            from GUI_pyqt import SEIHFR
            self.app2 = App(SEIHFR())
        elif (model_name == "SEIHFBR"):
            from GUI_pyqt import SEIHFBR
            self.app2 = App(SEIHFBR())
        elif (model_name == "Dispersion spatiale"):
            from PixelGrid import PixelGridWindow
            self.app2 = PixelGridWindow()
        elif (model_name == "Effet du vaccin"):
            from VaccineGrid import PixelGridWindowVaccined
            self.app2 = PixelGridWindowVaccined()
        elif (model_name == "Map"):
            from clean_map import MapWindow
            self.close()
            self.app2 = MapWindow("ccrs."+self.comboMap.currentText()+"()")
        self.close()


    def showNewCombo(self):
        self.hbox.addWidget(self.comboMap)
        self.comboMap.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())