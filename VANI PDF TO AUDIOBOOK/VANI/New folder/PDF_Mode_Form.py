# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\ZEEL_DATA\Python_Project\VANI PDF TO AUDIOBOOK\VANI\PDF_Mode_Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyttsx3
import PyPDF2


class Ui_PDF_Mode_Form(object):
    def setupUi(self, PDF_Mode_Form):
        PDF_Mode_Form.setObjectName("PDF_Mode_Form")
        PDF_Mode_Form.setWindowModality(QtCore.Qt.NonModal)
        PDF_Mode_Form.resize(600, 120)
        PDF_Mode_Form.setMinimumSize(QtCore.QSize(600, 120))
        PDF_Mode_Form.setMaximumSize(QtCore.QSize(600, 120))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\\ZEEL_DATA\\Python_Project\\VANI PDF TO AUDIOBOOK\\VANI\\../icons/audiobook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PDF_Mode_Form.setWindowIcon(icon)
        self.btn_audio = QtWidgets.QPushButton(PDF_Mode_Form)
        self.btn_audio.setGeometry(QtCore.QRect(450, 70, 111, 31))
        self.btn_audio.setObjectName("btn_audio")
        self.lineEdit = QtWidgets.QLineEdit(PDF_Mode_Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_browse = QtWidgets.QPushButton(PDF_Mode_Form)
        self.btn_browse.setGeometry(QtCore.QRect(450, 20, 111, 31))
        self.btn_browse.setObjectName("btn_browse")
        self.Page_No = QtWidgets.QSpinBox(PDF_Mode_Form)
        self.Page_No.setGeometry(QtCore.QRect(250, 70, 171, 31))
        self.Page_No.setMaximum(1000000000)
        self.Page_No.setObjectName("Page_No")
        self.label = QtWidgets.QLabel(PDF_Mode_Form)
        self.label.setGeometry(QtCore.QRect(20, 70, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(PDF_Mode_Form)
        QtCore.QMetaObject.connectSlotsByName(PDF_Mode_Form)

        self.btn_browse.clicked.connect(self.BrowseFile)
        self.btn_audio.clicked.connect(self.Speak)

    def BrowseFile(self):
        filename , _ = QtWidgets.QFileDialog.getOpenFileName(None,"Select PDF File","","File type  (*.pdf)")
        self.lineEdit.setText(filename)
        file = self.lineEdit.text()
        if file:
            self.book = open(file,'rb')
        else:
            self.book = 'please insert the PDF so i can read and remember    zeel is the best'

        self.pdfReader = PyPDF2.PdfFileReader(self.book)
        self.pages = self.pdfReader.numPages    
           
    def Speak(self):

        if self.lineEdit.text():

            speacker = pyttsx3.init()
            for num in range(int(self.Page_No.text()),self.pages):
                page = self.pdfReader.getPage(num)
                text = page.extractText()
                speacker.say(text)
                speacker.runAndWait()

        else:
            text = 'please insert the PDF so i can read and remember    zeel is the best'
            speacker = pyttsx3.init()
            speacker.say(text)
            speacker.runAndWait()

    def retranslateUi(self, PDF_Mode_Form):
        _translate = QtCore.QCoreApplication.translate
        PDF_Mode_Form.setWindowTitle(_translate("PDF_Mode_Form", "PDF Mode"))
        self.btn_audio.setText(_translate("PDF_Mode_Form", "Audio"))
        self.btn_browse.setText(_translate("PDF_Mode_Form", "Browse"))
        self.label.setText(_translate("PDF_Mode_Form", "Start From Page No :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PDF_Mode_Form = QtWidgets.QFrame()
    ui = Ui_PDF_Mode_Form()
    ui.setupUi(PDF_Mode_Form)
    PDF_Mode_Form.show()
    sys.exit(app.exec_())
