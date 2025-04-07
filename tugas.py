from PyQt5 import QtCore, QtGui, QtWidgets
import re
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Informasi Identitas di pojok kiri atas
        self.identity_label = QtWidgets.QLabel(self.centralwidget)
        self.identity_label.setGeometry(QtCore.QRect(10, 10, 300, 60))
        self.identity_label.setObjectName("identity_label")
        self.identity_label.setText(
            "Nama : Apta Mahogra Bhamakerti\nNIM  : F1D022035\nKelas: C"
        )
        self.identity_label.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))

        y_offset = 100  # Mulai agak di bawah identitas

        # Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, y_offset, 100, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, y_offset + 40, 100, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, y_offset + 80, 100, 20))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, y_offset + 120, 100, 20))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, y_offset + 160, 100, 20))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, y_offset + 240, 100, 20))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, y_offset + 280, 100, 20))
        self.label_7.setObjectName("label_7")

        # Input Fields
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, y_offset, 200, 25))

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, y_offset + 40, 200, 25))

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, y_offset + 80, 200, 25))

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, y_offset + 120, 200, 25))

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, y_offset + 160, 200, 60))

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, y_offset + 240, 200, 25))
        self.comboBox.addItems(["", "Male", "Female", "Other"])

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(200, y_offset + 280, 200, 25))
        self.comboBox_2.addItems(["", "High School", "Diploma", "Bachelor", "Master", "Doctorate"])

        # Buttons
        self.pushButton = QtWidgets.QPushButton("Save", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, y_offset + 330, 90, 30))
        self.pushButton_2 = QtWidgets.QPushButton("Clear", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, y_offset + 330, 90, 30))

        # Connect buttons
        self.pushButton.clicked.connect(self.save_data)
        self.pushButton_2.clicked.connect(self.clear_fields)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form Validation"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Age:"))
        self.label_4.setText(_translate("MainWindow", "Phone Number:"))
        self.label_5.setText(_translate("MainWindow", "Address:"))
        self.label_6.setText(_translate("MainWindow", "Gender:"))
        self.label_7.setText(_translate("MainWindow", "Education:"))

    def save_data(self):
        name = self.lineEdit.text()
        email = self.lineEdit_2.text()
        age = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()
        address = self.textEdit.toPlainText()
        gender = self.comboBox.currentText()
        education = self.comboBox_2.currentText()

        # Validasi
        if not name:
            self.show_error("Please enter a valid name.")
            return
        if not re.match(r"[^@]+@gmail\.com$", email):
            self.show_error("Please enter a valid Gmail address.")
            return
        if not age.isdigit():
            self.show_error("Please enter a valid age (digits only).")
            return
        if not re.fullmatch(r"\+62\d{11}", phone.replace(" ", "")):
            self.show_error("Please enter a valid phone number with +62 and 13 digits.")
            return
        if not address:
            self.show_error("Please enter a valid address.")
            return
        if not gender:
            self.show_error("Please select a gender.")
            return
        if not education:
            self.show_error("Please select an education level.")
            return

        QMessageBox.information(None, "Success", "Data saved successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.textEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)

    def show_error(self, message):
        QMessageBox.warning(None, "Input Error", message)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            QtWidgets.QApplication.quit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
